import requests
import json
from collections import namedtuple
from contextlib import closing
import sqlite3
import datetime
import subprocess
from prefect import task, Flow
from prefect.tasks.database.sqlite import SQLiteScript
from prefect.schedules import IntervalSchedule
from prefect.engine import signals
from prefect.engine.results import LocalResult

def alert_failed(obj, old_state,new_state):
    if new_state.is_failed():
        print("Failed!")
##setup
create_table = SQLiteScript(
    db='cfpbcomplaints.db',
    script='CREATE TABLE IF NOT EXISTS complaint (timestamp TEXT, state TEXT, product TEXT, company TEXT, complaint_what_happened TEXT)'
)

@task()
def spam():
    exec(open("spamGenerator.py").read())


## extract
@task(cache_for=datetime.timedelta(days=1), state_handlers=[alert_failed])
def get_complaint_data():
    r = requests.get("https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/", params={'size':10})
    response_json = json.loads(r.text)
    print("i actually requested this time!")
    return response_json['hits']['hits']

## transform
@task (state_handlers=[alert_failed])
def parse_complaint_data(raw):
    #raise signals.SUCCESS
    #raise Exception
    complaints = []
    Complaint = namedtuple('Complaint', ['data_received', 'state', 'product', 'company', 'complaint_what_happened'])
    for row in raw:
        source = row.get('_source')
        this_complaint = Complaint(
            data_received=source.get('date_recieved'),
            state=source.get('state'),
            product=source.get('product'),
            company=source.get('company'),
            complaint_what_happened=source.get('complaint_what_happened')
        )
        complaints.append(this_complaint)
    return complaints

## load
@task(state_handlers=[alert_failed])
def store_complaints(parsed):
    create_script = 'CREATE TABLE IF NOT EXISTS complaint (timestamp TEXT, state TEXT, product TEXT, company TEXT, complaint_what_happened TEXT)'
    insert_cmd = "INSERT INTO complaint VALUES (?, ?, ?, ?, ?)"

    with closing(sqlite3.connect("cfpbcomplaints.db")) as conn:
        with closing(conn.cursor()) as cursor:
            #cursor.executescript(create_script)
            cursor.executemany(insert_cmd, parsed)
            conn.commit()

schedule=IntervalSchedule(interval=datetime.timedelta(minutes=1))

with Flow("Mi Workflow-Victor Velasco",schedule) as f:
    db_table = create_table()
    raw = get_complaint_data()
    parsed = parse_complaint_data(raw)
    populated_table=store_complaints(parsed)
    populated_table.set_upstream(db_table)
    store_complaints(parsed)
    #subprocess.call("spamGenerator.py", shell=True)
    #exec(open("spamGenerator.py").read())
    spam()

f.register(project_name="Introduction")
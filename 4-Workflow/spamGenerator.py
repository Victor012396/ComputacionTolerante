import smtplib
import os

#Variable de entorno
PASSWORD_APP=os.environ.get('-')
EMAIL= os.environ.get('-')

#Establecer conexión al servidor de correos SMTP
conexion=smtplib.SMTP(host='smtp.gmail.com', port=587)
conexion.ehlo()

#Encriptacion TLS
conexion.starttls()

#Iniciar sesión en el servidor SMTP
conexion.login(user="-", password='-')

#Enviar correo
mensaje='Subject:Correo de Prueba\nEsto es una prueba'
conexion.sendmail(from_addr="-",to_addrs="-",msg=mensaje)

#Desconectar del servidor SMTP
conexion.quit()

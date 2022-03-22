package org.victor.controller;

import org.eclipse.microprofile.faulttolerance.*;
import org.victor.model.Person;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.logging.Logger;

import static java.util.List.of;


@Path("/persons")
@Produces(MediaType.APPLICATION_JSON)

public class PersonController {

    List<Person> personList = new ArrayList<>();
    Logger LOGGER = Logger.getLogger("Demologger");
    @GET
    //@Timeout(value = 5000L)
    //@Retry(maxRetries = 4)
    @CircuitBreaker(failureRatio = 0.1,delay=1500L)
    //@Bulkhead(value = 1)
    @Fallback(fallbackMethod = "getPersonFallbackList")
    public List<Person> getPersonList(){
        //doWait();
        doFail();
        return this.personList;
    }

    public List<Person> getPersonFallbackList(){
        var person=new Person((long) -1,"Victor","victor.com");
        return List.of(person);
    }

    public void doWait(){
        var random= new Random();
        try{
            LOGGER.warning("Haciendo sleep");
            Thread.sleep((random.nextInt(10)+4)*1000L);
        }catch(Exception e){

        }

    }

    public void doFail(){
        var random= new Random();
        if(random.nextBoolean()){
            LOGGER.warning("Se produce una falla");
            throw new RuntimeException("Implementación fallida");
        }
    }

}

package org.victor.controller;

import org.eclipse.microprofile.faulttolerance.CircuitBreaker;
import org.eclipse.microprofile.faulttolerance.Fallback;
import org.victor.model.RFC;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.logging.Logger;

@Path("/rfc")
@Produces(MediaType.APPLICATION_JSON)

public class RFController {
    List<RFC> rfcList=new ArrayList<>();
    Logger LOGGER=Logger.getLogger("RFClogger");

    @GET
    //@Timeout(value = 5000L)
    //@Retry(maxRetries = 4)
    @CircuitBreaker(failureRatio = 0.1,delay=1500L)
    //@Bulkhead(value = 1)
    @Fallback(fallbackMethod = "getRfcFallbackList")
    public List<RFC> getRfcList(){
        //esperar();
        fallo();
        return this.rfcList;
    }

    public List<RFC> getRfcFallbackList(){
        var rfc=new RFC("-","Usuario default","shcp@gob.mx");
        return List.of(rfc);
    }

    public void esperar(){
        var random= new Random();
        try{
            LOGGER.warning("Estado: Durmiente");
            Thread.sleep((random.nextInt(10)+4)*1000L);
        }catch(Exception e){

        }

    }

    public void fallo(){
        var random= new Random();
        if(random.nextBoolean()){
            LOGGER.warning("Se produjo una falla");
            throw new RuntimeException("Implementación fallida");
        }
    }





}

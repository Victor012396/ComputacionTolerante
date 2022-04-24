package org.victor.controller;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

@Path("/CUCEI")
public class GreetingResource {

    @GET//ds
    @Produces(MediaType.TEXT_PLAIN)
    public String hello() {
        return "This homework was created by Victor Velasco";
    }
}
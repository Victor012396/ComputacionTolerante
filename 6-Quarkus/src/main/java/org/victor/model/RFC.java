package org.victor.model;

public class RFC {
    private String rfcid;
    private String name;
    private String email;
    public RFC(String i, String user, String s){
        this.rfcid=i;
        this.name=user;
        this.email=s;
    }
    public String getRfcid() {
        return rfcid;
    }

    public void setRfcid(String rfcid) {
        this.rfcid = rfcid;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }


}

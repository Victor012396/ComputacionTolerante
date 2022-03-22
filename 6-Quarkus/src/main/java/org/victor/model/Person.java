package org.victor.model;

public class Person {
    private Long personId;
    private String name;
    private String email;

    public Person(Long i, String victor, String s) {
        this.personId = i;
        this.name=victor;
        this.email=s;
    }

    public Long getPersonId() {
        return personId;
    }

    public void setPersonId(Long personId) {
        this.personId = personId;
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

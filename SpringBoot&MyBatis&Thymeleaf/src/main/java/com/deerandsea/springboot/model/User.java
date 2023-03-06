package com.deerandsea.springboot.model;

import lombok.Data;

import java.io.Serializable;

@Data
public class User implements Serializable {
    private Integer id;
    private String name;
    private String email;
    // getter and setter methods

}

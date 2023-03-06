package com.deerandsea.javasimpleserver.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class Controller {

    @GetMapping(value = "/", name = "Hello World")
    public String hello(@RequestParam(value = "name", required = false) String name) {
        return String.format("Hello %s! ", name == null ? "World" : name);
    }
}


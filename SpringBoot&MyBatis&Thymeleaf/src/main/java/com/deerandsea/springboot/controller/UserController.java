package com.deerandsea.springboot.controller;

import com.deerandsea.springboot.model.User;
import com.deerandsea.springboot.mapper.UserMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

import java.util.List;

@Controller
public class UserController {
    @Autowired
    private UserMapper userMapper;

    @GetMapping("/")
    public String list(Model model) {
        List<User> userList = userMapper.findAll();
        model.addAttribute("userList", userList);
        return "user/list";
    }

    @GetMapping("/add")
    public String add(Model model) {
        model.addAttribute("user", new User());
        return "user/add";
    }

    @PostMapping("/add")
    public String save(User user) {
        userMapper.save(user);
        return "redirect:/";
    }
}

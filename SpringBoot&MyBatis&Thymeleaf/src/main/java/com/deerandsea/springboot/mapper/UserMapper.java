package com.deerandsea.springboot.mapper;

import com.deerandsea.springboot.model.User;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;


@Mapper
public interface UserMapper {
    List<User> findAll();
    void save(User user);
}

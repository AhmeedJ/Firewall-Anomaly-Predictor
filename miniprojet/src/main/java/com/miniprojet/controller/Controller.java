package com.miniprojet.controller;

import com.miniprojet.model.DataAnalyzed;
import com.miniprojet.service.IDataAnalyzeServices;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@CrossOrigin("*")
@RequestMapping("/tosaveapi/data")
public class Controller {
    @Autowired
    IDataAnalyzeServices iDataAnalyzeServices;

    @PostMapping("/add")
    public void addAnalyzedData(@RequestBody DataAnalyzed dataAnalyzed) {
        iDataAnalyzeServices.addAnalyzedData(dataAnalyzed);
    }
    @GetMapping("/all")
    public List<DataAnalyzed> returnAnalyzedData() {
        return iDataAnalyzeServices.returnAnalyzedData();
    }

}

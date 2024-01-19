package com.miniprojet.service;

import com.miniprojet.model.DataAnalyzed;
import com.miniprojet.repository.IdataAnalyzeRepo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

@Service
public class DataAnalyzeServices implements IDataAnalyzeServices{

    @Autowired
    IdataAnalyzeRepo idataAnalyzeRepo;

    @Override
    public void addAnalyzedData(DataAnalyzed dataAnalyzed){
        try {
            idataAnalyzeRepo.save(dataAnalyzed);
        } catch (Exception e) {
            System.err.println("Error saving analyzed data: " + e.getMessage());
        }
    }

    @Override
    public List<DataAnalyzed> returnAnalyzedData() {
        try {
            List<DataAnalyzed> dataAnalyzedList = idataAnalyzeRepo.findAll();
            return dataAnalyzedList;
        } catch (Exception e) {
            System.err.println("Error retrieving analyzed data: " + e.getMessage());
            return Collections.emptyList();
        }
    }

}

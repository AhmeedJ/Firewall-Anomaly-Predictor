package com.miniprojet.service;

import com.miniprojet.model.DataAnalyzed;

import java.util.List;

public interface IDataAnalyzeServices {
    void addAnalyzedData(DataAnalyzed dataAnalyzed);
    List<DataAnalyzed> returnAnalyzedData();


}

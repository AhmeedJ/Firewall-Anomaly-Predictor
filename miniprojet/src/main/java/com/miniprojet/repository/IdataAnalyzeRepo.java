package com.miniprojet.repository;

import com.miniprojet.model.DataAnalyzed;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface IdataAnalyzeRepo extends JpaRepository<DataAnalyzed, Long> {

}

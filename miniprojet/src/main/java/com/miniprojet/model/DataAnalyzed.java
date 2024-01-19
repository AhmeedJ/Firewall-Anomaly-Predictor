package com.miniprojet.model;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Entity
@Table(name = "t_dataAnalyzed")
@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class DataAnalyzed {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private float protocol_type;
    private float service;
    private float flag;
    private float src_bytes;
    private float dst_bytes;
    private float count;
    private float same_srv_rate;
    private float diff_srv_rate;
    private float dst_host_srv_count;
    private float dst_host_same_srv_rate;
    private String result;
}



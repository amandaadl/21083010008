#!/bin/bash

echo "Indeks Prestasi Semester dan Indeks Prestasi Kumulatif"
echo "Nama : " 
read nama;
echo "Masukkan : "
read inputan;
read nilai1
read nilai2
read nilai3

let ips=$nilai1+$nilai2+$nilai3;
let ipk=($nilai1+$nilai2+$nilai3)/$inputan;

semester=($ips)
kumulatif=($ipk)

echo "IPS Mahasiswa : " ${semester[*]} "/" $inputan
echo "IPK Mahasiswa : " ${kumulatif[*]}

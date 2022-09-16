#!/bin/bash

#deklarasi array
distroLinux=("Mint" "Ubuntu" "Kali" "Arch" "Debian")

#random
let pilih=$RANDOM%5

#eksekusi
echo "Saya Memilih Distro $pilih, ${distroLinux[$pilih]} !"

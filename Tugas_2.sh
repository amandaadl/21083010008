#!/bin/bash

echo -n "Masukkan nilai anda :"
read nilai
if [ $nilai -gt 60 ]; then
echo "selamat anda lulus"
else
echo "anda gagal"
fi


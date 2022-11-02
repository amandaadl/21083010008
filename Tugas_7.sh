#!/bin/bash

panjang() {
	echo "Masukkan panjang :"
	read panjang
}
lebar() {
	echo "Masukkan lebar :"
	read lebar
}
luas() {
	let jumlah=$panjang*$lebar
	echo -e "Luas persegi panjang : $jumlah"
}

#memanggil fungsi
panjang
lebar
luas

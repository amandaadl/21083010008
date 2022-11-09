from os import getpid
from time import time,sleep
from multiprocessing import cpu_count, Pool, Process

def cetak(x):
        print("Cetak angka", x, "- punya ID proses", getpid())
        sleep(1)

sekuensial_awal = time()

print('Masukkan nilai awal dan nilai akhir')

nilai_awal = int(input(' nilai awal: '))
nilai_akhir = int(input(' nilai akhir: '))

print("""\nTampilkan bilangan
 1. Ganjil
 2. Genap""")

pilihan = int(input('Pilihan: '))

# periksa kalau pilihan bukan 1 dan 2
if pilihan not in [1, 2]:
  print('Pilihan salah')
else:
  for x in range(nilai_awal, nilai_akhir + 1):
    if pilihan == 1 and x % 2 == 1:
      print(cetak(x), " ")
    elif pilihan == 2 and x % 2 == 0:
      print(cetak(x), " ")
  else:
    # ganti baris ketika perulangan selesai
    print('')
sekuensial_akhir = time()

print("Sekuensial :", sekuensial_akhir - sekuensial_awal, "detik")

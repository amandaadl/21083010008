import os
import sys
total = []

def clear_screen():
    os.system('clear' if(os.name=='nt') else 'clear')
    
def kembali():
    print("\n")
    input("tekan tombol apa saja untuk kembali")
    clear_screen()
    
def keluar():
    print('-' * 32)
    print("*     LAKUKAN PEMBAYARAN     *")
    print('-' * 32)
    print("Terimakasih telah berkunjung  (:")
    
    
def menu_awal():
    while(True) :
        print("Selamat Datang di SALE SPACE")
        print("Sale Space menjual berbagai barang fashion impor dengan harga yang sangat terjangkau")
        print("Diskon mulai dari 20% hingga 60% dan juga dapatkan bonus selected item kami di semua pembelian tanpa minimum belanja")
        print('Silahkan Pilih Menu di Bawah Ini ❤️')
        print('-' * 32)
        print(' 1 Footwear')
        print(' 2 Clothes')
        print(' 3 Accessories')
        print(' 4 Daftar diskon')
        print(' 5 Pembayaran')
        print(' 6 Keluar')
        try:
            a = int(input('pilih menu 1-6:'))
            print()
            if (a==1):
                footwear()
                kembali()
            elif (a==2):
                clothes()
                kembali()
            elif (a==3):
                accessories()
                kembali()
            elif (a==4):
                daftar_diskon()
                kembali()
                break
            elif (a==5):
                akhir()
                break
            elif (a==6):
                keluar()
                break
            else:
                print('Masukkan angka 1-6')
                kembali()
                continue
        except ValueError:
            print('Masukkan sesuai yang ada di daftar menu!')
            kembali()
            continue
            
def footwear():
    print("                    DAFTAR DISKON                         ")
    print(" No |              Jumlah Belanja                 | Harga ")
    print("-" * 60)
    print(" 1  | > Rp  500000 & Voucher Cincau Station       | 20%    ")
    print(" 2  | > Rp 1000000 & Voucher Sushi Tei            | 40%   ")
    print(" 3  | > Rp 1500000 & Free Kaos Kaki               | 50%   ")
    print(" 4  | > Rp 2000000 & Free Sandal                  | 60%   ")
    print("-" * 60)
    print(" No |         Daftar Barang         | Harga ")
    print("-" * 45)
    print(" 1  | Sepatu Olahraga               |  999000")
    print(" 2  | Sepatu Hiking                 | 1499000")
    print(" 3  | Sneakers                      | 1299000")
    print(" 4  | Sandal                        |  199000")
    print(" 5  | Kaos Kaki                     |   50000")
    print(" 6  | Tali Sepatu                   |   29000")
    print("-" * 45)
    kode = int(input("Masukkan no barang :"))
    if (kode==1):
        jumlah1 = int(input("Masukkan jumlah barang :"))
        total1 = 999000*jumlah1
        total.append(total1)
        tanya()
    elif (kode==2):
        jumlah2 = int(input("Masukkan jumlah barang :"))
        total2 = 1499000*jumlah2
        total.append(total2)
        tanya()
    elif (kode==3):
        jumlah3 = int(input("Masukkan jumlah barang :"))
        total3 = 1299000*jumlah3
        total.append(total3)
        tanya()
    elif (kode==4):
        jumlah4 = int(input("Masukkan jumlah barang :"))
        total4 = 199000*jumlah4
        total.append(total4)
        tanya()
    elif (kode==5):
        jumlah5 = int(input("Masukkan jumlah barang :"))
        total5 = 50000*jumlah5
        total.append(total5)
        tanya()
    elif (kode==6):
        jumlah6 = int(input("Masukkan jumlah barang :"))
        total6 = 29000*jumlah6
        total.append(total6)
        tanya()
    return

def clothes():
    print("                    DAFTAR DISKON                         ")
    print(" No |              Jumlah Belanja                 | Harga ")
    print("-" * 60)
    print(" 1  | > Rp  500000 & Voucher Cincau Station       | 20%    ")
    print(" 2  | > Rp 1000000 & Voucher Sushi Tei            | 40%   ")
    print(" 3  | > Rp 1500000 & Free Kaos Kaki               | 50%   ")
    print(" 4  | > Rp 2000000 & Free Sandal                  | 60%   ")
    print("-" * 60)
    print(" No |         Daftar Barang         | Harga ")
    print("-" * 45)
    print(" 1  | High End Brands               | 2499000")
    print(" 2  | Premium Brands                | 1499000")
    print(" 3  | Middle Brands                 |  500000")
    print("-" * 45)
    kode = int(input("Masukkan no barang :"))
    if (kode==1):
        jumlah1 = int(input("Masukkan jumlah barang :"))
        total1 = 2499000*jumlah1
        total.append(total1)
        tanya()
    elif (kode==2):
        jumlah2 = int(input("Masukkan jumlah barang :"))
        total2 = 1499000*jumlah2
        total.append(total2)
        tanya()
    elif (kode==3):
        jumlah3 = int(input("Masukkan jumlah barang :"))
        total3 = 500000*jumlah3
        total.append(total3)
        tanya()
    return

def accessories():
    print("                    DAFTAR DISKON                         ")
    print(" No |              Jumlah Belanja                 | Harga ")
    print("-" * 60)
    print(" 1  | > Rp  500000 & Voucher Cincau Station       | 20%    ")
    print(" 2  | > Rp 1000000 & Voucher Sushi Tei            | 40%   ")
    print(" 3  | > Rp 1500000 & Free Kaos Kaki               | 50%   ")
    print(" 4  | > Rp 2000000 & Free Sandal                  | 60%   ")
    print("-" * 60)
    print(" No |      Daftar Barang      |  Harga ")
    print("-" * 45)
    print(" 1  | Necklace                | 149000")
    print(" 2  | Bracelet                | 100000")
    print(" 3  | Ring                    |  50000")
    print("-" * 45)
    kode = int(input("Masukkan no barang :"))
    if (kode==1):
        jumlah1 = int(input("Masukkan jumlah barang :"))
        total1 = 149000*jumlah1
        total.append(total1)
        tanya()
    elif (kode==2):
        jumlah2 = int(input("Masukkan jumlah barang :"))
        total2 = 100000*jumlah2
        total.append(total2)
        tanya()
    elif (kode==3):
        jumlah3 = int(input("Masukkan jumlah barang :"))
        total3 = 50000*jumlah3
        total.append(total3)
        tanya()
    return

def daftar_diskon():
    print(" No |              Jumlah Belanja                 | Harga ")
    print("-" * 60)
    print(" 1  | > Rp  500000 & Voucher Cincau Station       | 20%    ")
    print(" 2  | > Rp 1000000 & Voucher Sushi Tei            | 40%   ")
    print(" 3  | > Rp 1500000 & Free Kaos Kaki               | 50%   ")
    print(" 4  | > Rp 2000000 & Free Sandal                  | 60%   ")
    print("-" * 60)
    
def tanya():
    print("---------------------------------------")
    tanya = input("ingin tambah barang? [Y/T] :")
    print("---------------------------------------")
    if (tanya=="Y"):
        menu_awal()
    elif (tanya=="T"):
        akhir()
    else:
        print("Pilihan yang anda masukkan salah!")
           
def akhir():
    print("SubTotal     :", sum(total))
    diskon=0
    a=sum(total)
    if(a>=2000000):
        diskon=0.6
        print("Diskon 60% dan Free Sandal")
    elif(a>=1000000):
            diskon=0.5
            print("Diskon 50% dan Free Kaos Kaki")
    elif(a>=1500000):
            diskon=0.4
            print("Diskon 40% dan Voucher Sushi Tei")
    elif(a>=500000):
            diskon=0.2
            print("Diskon 20% dan Voucher Cincau Station")
    else:
        diskon=0
    potongan = a*diskon
    print("Potongan Harga Sebesar :", potongan) 
    totalakhir = a - (a*diskon)
    print("Total           :", totalakhir)
    print("-------------------------------")
    bayar = int(input("Jumlah Pembayaran :"))
    kembalian = bayar-totalakhir
    print("Kembalian       :", kembalian)
    print("-------------------------------")
    print("          Terima Kasih         ")
    print("-------------------------------")
menu_awal()

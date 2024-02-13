Tugas Kecil 1 IF 2211 Strategi Algortima

A). Deskripsi Singkat
Program merupakan solver untuk minigame Hacking di game Cyberpunk 2077 yang menggunakan algoritma brute force.

B). Requirement
  - Python (versi yang digunakan : 3.11.0)
  - Numpy (versi yang digunakan : 12.6.1)

C). Cara Menggunakan
  - Input
      Pengguna perlu menginput data sebagai berikut : Matrix,Ukuran Buffer,Sekuens,Reward untuk Sekuens.
      Ada 2 cara menginput, pertama melalui file txt dengan format dibawah ini, yang kedua adalah dengan randomize. 
      Untuk menggunakan fitur randomize pengguna perlu menginput token yang diinginkan untuk muncul pada matrix dan sekuens,
      banyak baris dan kolom dari matriks, ukuran buffer, dan ukuran maksimum sekuens

      contoh format file
      7 # ukuran buffer
      6 6 # baris kolom
      7A 55 E9 E9 1C 55  # matriks
      55 7A 1C 7A E9 55
      55 1C 1C 55 E9 BD
      BD 1C 7A 1C 55 BD
      BD 55 BD 7A 1C 1C
      1C 55 55 7A 55 7A
      3 # banyak sekuens
      BD E9 1C  #sekuens ke-1
      15 # reward sekuen ke-1
      BD 7A BD
      20
      BD 1C BD 55
      30
      
  - Output
      setelah selesai menginput dan klik enter, solusi akan keluar dengan format dibawah ini

      50 # Reward maximum
      7A BD 7A BD 1C BD 55 # isi buffer
      1, 1 # koordinat dari setiap elemen pada buffer dalam matriks (x, y)
      1, 4
      3, 4
      3, 5
      6, 5
      6, 4
      5, 4
      300 ms # waktu memproses
      Apakah ingin menyimpan solusi? (y/n) # opsi untuk menympan solusi

  3). Save
      setelah keluar solusi, pengguna memiliki opsi untuk menyimpan solusi kedalan file, format solusi yang di simpan menyerupai Output

D). Identitas Pembuat Program
   -  Nama : Pradipta Rafa Mahesa
   -  NIM : 13522162
   -  Kelas : K3


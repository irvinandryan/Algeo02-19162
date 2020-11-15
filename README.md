# AID SEARCH!
> AID Search! merupakan website yang dikembangkan oleh kelompok 17 sebagai tugas besar mata kuliah Aljabar Linear dan Geometri berupa search engine

## Table of contents
* [General info](#general-info)
* [Setup](#setup)
* [Usage](#usage)
* [Features](#features)
* [Status](#status)
* [Inspiration](#inspiration)
* [Contact](#contact)

## General info
AID Search! adalah website yang dikembangkan oleh kelompok 17 sebagai tugas besar mata kuliah Aljabar Linear dan Geometri tahun ajaran 2020/2021 berupa search engine. Search engine yang kelompok kami buat menggunakan bahasa pemrograman python dan menggunakan flask. Search engine yang kami buat menggunakan rumus cosine similarity untuk mencari kecocokan antar query dengan dokumen dan menampilkan dokumen yang paling tinggi tingkat kecocokannya dengan query, dan seterusnya berurut semakin rendah similarity nya. Ditampilkan pula tabel term yang akan menampilkan term-term yang menentukan similarity sebuah queue dengan dokumen.



## Setup
Berikut cara melakukan instalasi pada OS Windows/MacOS:
1. Download terlebih dahulu repository ini untuk mendapatkan file dari kelompok kami.
2. Pastikan python 3 dan pip sudah terinstall di perangkat dan sudah masuk ke local environment. (Untuk mengeceknya ketik "python --version" dan "pip --version" di cmd)
3. Install stemmer Sastrawi menggunakan pip. (ketik "pip install Sastrawi" di cmd)
4. Install pula Flask untuk mengakses search engine tersebut. (ketik "pip install flask" di cmd)
5. Setelah itu di cmd, ubah directory menuju folder repository ini --> src (contoh "cd C:\github\Algeo02-19162\src" untuk OS Windows dan "cd ~/github/Algeo02-19162/src" untuk Mac OS)
6. Ketik "set FLASK_APP=webflask.py" jika menggunakan sistem operasi Windows atau "export FLASK_APP=webflask.py" jika menggunakan sistem operasi mac OS untuk mengatur penggunaan Flask
7. Ketik "set FLASK_ENV=development" untuk mengatur environment dan mengubah status dari production menjadi development (khusus sistem operasi Windows)
8. Ketik "Flask run", dan akan timbul pesan seperti berikut: "Running on http://127.0.0.1:5000/",
9. Copy alamat tersebut (http://127.0.0.1:5000/) dan jalankan alamat tersebut di browser manapun. Tunggu proses initializing-nya kisaran 1 menit.
10. AID Search! siap untuk digunakan.

## Usage
1. Setelah mengetik "Flask run", program akan melakukan inisialisasi data dengan mengambil semua dokumen dalam folder test. Folder test hanya diisi oleh file dengan format ".txt" dimana nama file akan adalah judul dokumen yang dipisah dengan underscore ("\_"). Proses inisialisasi ditunjukkan oleh "initializing..." yang tercetak pada terminal/cmd.
2. Saat AID Search! berhasil ditampilkan pada browser, program siap digunakan. Ketik string yang ingin dicari dalam kolom "Masukkan Query" lalu tekan tombol "Search" untuk menjalankan pencarian.
3. Untuk menambahkan dokumen ke daftar dokumen yang ingin dicari, tekan tombol "Upload Files" di main page. Akan muncul tombol "browse" dan "upload" di layar. Tekan "browse" untuk mencari file, pastikan nama file tersebut benar melalui tampilan yang muncul, lalu tekan "upload" untuk menyimpan file.
4. Saat melakukan search setelah upload file, program akan menambahkan dokumen-dokumen baru ke daftar dokumen dan muncul "reloading..." di cmd. Tunggu proses reloading-nya kisaran 1 menit.
5. Setelah hasil search berhasil ditampilkan oleh program, judul dokumen yang ditampilkan pada hasil search dapat ditekan untuk membuka isi dokumennya.
6. Untuk mengetahui informasi mengenai AID Search!, tekan tulisan "Perihal" pada bagian bawah halaman.
7. Untuk kembali ke halaman main page, tekan tulisan "AID Search!" pada bagian atas halaman.
8. Untuk keluar dari program, buka terminal/cmd yang sedang menjalankan webflask.py dan tekan tombol "CTRL" dan "C" secara bersamaan.
9. File .txt yang telah diupload saat menjalankan program akan tetap disimpan dalam folder test.

## Features
Beberapa list fitur dari program ini:
* Program search engine menggunakaan cosine similarity
* Upload file ke dalam server sehingga dapat digunakan kemudian

## Status
Project is: _finished_ karena deadline-nya tanggal 16 November 2020

## Inspiration
Terima kasih sebesar-besarnya kepada Bapak/Ibu dosen pengampu mata kuliah Aljabar Linear dan Geometri yang sudah berjasa dalam membimbing dan memberi kami ilmu.

## Contact
1. Irvin Andryan Pratomo      / 13519162
2. Muhammad Dehan Al Kautsar  / 13519200
3. Muhammad Rifat Abiwardani  / 13519205
Kelompok 17 Algeo

# AID SEARCH!
> AID Search! merupakan website yang dikembangkan oleh kelompok 17 sebagai tugas besar mata kuliah Aljabar Linear dan Geometri berupa search engine

## Table of contents
* [General info](#general-info)
* [Setup](#setup)
* [Features](#features)
* [Status](#status)
* [Inspiration](#inspiration)

## General info
AID Search! adalah website yang dikembangkan oleh kelompok 17 sebagai tugas besar mata kuliah Aljabar Linear dan Geometri tahun ajaran 2020/2021 berupa search engine. Search engine yang kelompok kami buat menggunakan bahasa pemrograman python dan menggunakan flask. Search engine yang kami buat menggunakan rumus cosine similarity untuk mencari kecocokan antar query dengan dokumen dan menampilkan dokumen yang paling tinggi tingkat kecocokannya dengan query, dan seterusnya berurut semakin rendah similarity nya. Ditampilkan pula tabel term yang akan menampilkan term-term yang menentukan similarity sebuah queue dengan dokumen.



## Setup
Describe how to install / setup your local environement / add link to demo version.
Berikut cara melakukan instalasi pada OS Windows:
1. Pastikan python dan pip sudah terinstall di perangkat dan sudah masuk ke local environment. (Untuk mengeceknya ketik "python --version" dan "pip --version" di cmd)
2. Install stemmer Sastrawi menggunakan pip. (ketik "pip install Sastrawi" di cmd)
3. Install pula Flask untuk mengakses search engine tersebut. (ketik "pip install flask" di cmd)
4. Setelah itu di cmd, ubah directory menuju folder repository ini.
5. Ketik "set FLASK_APP=webflask.py" untuk mengatur penggunaan Flask
6. Ketik "set FLASK_ENV=development" untuk mengatur environment dan mengubah status dari production menjadi development
7. Ketik "Flask run", dan akan timbul pesan seperti berikut: "Running on http://127.0.0.1:5000/",
8. Copy alamat tersebut (http://127.0.0.1:5000/) dan jalankan alamat tersebut di browser manapun. Tunggu proses initializing-nya kisaran 1 menit.
9. AID Search! siap untuk digunakan.

## Code Examples
Show examples of usage:
`put-your-code-here`

## Features
Beberapa list fitur dari program ini:
* Program search engine menggunakaan cosine similarity
* Upload file ke dalam server sehingga dapat digunakan kemudian

## Status
Project is: _finished_ karena deadline-nya tanggal 16 November 2020

## Inspiration
Terima kasih sebesar-besarnya kepada Bapak/Ibu dosen pengampu mata kuliah Aljabar Linear dan Geometri yang sudah berjasa dalam membimbing dan memberi kami ilmu.

# KIJ-F07
Tugas 1 - Implementasi algoritma Data Encryption Standard (DES) dengan menggunakan mode operasi Counter (CTR)

Kelompok F07 :
- Lucha Kamala P. (5114100062)
- Irfan Hanif     (5114100177)

## Pendahuluan
Seiring dengan perkembangan teknologi informasi secara pesat pada era globalisasi sekarang, informasi dapat dengan mudah untuk didapatkan. Berdasarkan oleh berbagai kemudahan yang ditawarkan bagi pengguna teknologi informasi, pengguna teknologi inipun mengalami kenaikan pesat. Bertambahnya pengguna internet pada saat ini juga mendorong berbagai tindak kejahatan dalam penggunaan teknologi informasi.

Pada suatu sistem jaringan, arus komunikasi data dan keamanan informasi merupakan hal pokok yang harus dijaga. Informasi penting yang dikirimkan melalui jaringan beresiko mengalami penyadapan dan bahkan pengubahan data asli yang sering dilakukan oleh orang-orang yang tidak bertanggung jawab. Oleh karena itu, untuk menghindari hal tersebut, kita harus melakukan pencegahan dan pengamanan agar dapat mengurangi gangguan terhadap keamanan informasi pada arus komunikasi data dalam sistem jaringan.

Salah satu cara yang dapat dilakukan untuk menjaga kerahasiaan data dan keamanan informasi pada jaringan adalah dengan melakukan teknik ekripsi. Enkripsi adalah proses mengamankan suatu informasi dengan cara mengubah informasi asli (disebut dengan plaintext) menjadi informasi yang terenkripsi (disebut dengan chipertext) dengan menggunakan kunci pada operasi algoritma tertentu, sehingga informasi asli tersebut tidak dapat diketahui secara langsung. Berkebalikan dengan proses enkripsi, proses dekripsi digunakan untuk mengembalikan informasi yang terenkripsi (chipertext) menjadi informasi asli (plaintext).

Terdapat banyak algoritma yang digunakan sebagai metode enkripsi dan dekripsi, salah satunya adalah algoritma Data Encryption Standard (DES) dengan menggunakan mode operasi Counter (CTR).

## Dasar Teori
### Data Encryption Standard
Pada bidang kriptografi, Data Encryption Standard (DES) adalah algoritma enkripsi kunci simetrik dan tergolong dalam jenis block cipher. Algoritma ini digunakan untuk mengenkripsi suatu blok plaintext berukuran 64-bit menjadi ciphertext berukuran 64-bit dengan menggunakan kunci berukuran 56-bit.

<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/24416774/151755e4-1410-11e7-9915-ef648ed8ac24.png" /></p> 
### Counter
Counter (CTR) merupakan salah satu mode operasi yang digunakan untuk mengubah block cipher menjadi stream chipher. Mode operasi ini menghasilkan blok keystream selanjutnya dengan mengenkripsi nilai berkelanjutan dari suatu “counter”. Counter tersebut dapat berupa fungsi apapun yang mengeluarkan suatu sekuens yang menjamin tidak akan berulang dalam jangka waktu panjang. Meskipun demikian, jenis counter biasa (1, 2, 3, … dan seterusnya) lebih mudah dan sering digunakan. Mode Counter (CTR) sangat cocok untuk dioperasikan pada komputer multi-processor, dimana blok dapat diekripsikan secara pararel. Selain itu, mode ini juga tidak mengalami permasalahan short-cycle.

<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/24415268/1a5550ba-140b-11e7-92da-d8b3fa384ab9.png" /></p>

<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/24416039/99f93a82-140d-11e7-8e2f-946ffdec317d.png" /></p>

## Langkah Implementasi
Berikut ini merupakan langkah implementasi algoritma Data Encryption Standard (DES) dengan menggunakan mode operasi Counter (CTR):
1. Langkah pertama adalah
2. Langkah kedua adalah

## Kesimpulan

## Saran

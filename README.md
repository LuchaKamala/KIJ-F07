# KIJ-F07
Tugas 1 - Implementasi algoritma Data Encryption Standard (DES) dengan menggunakan mode operasi Counter (CTR)

Kelompok F07 :
- Lucha Kamala P. (5114100062)
- Irfan Hanif     (5114100177)

## Pendahuluan
Seiring dengan perkembangan teknologi informasi secara pesat, informasi dapat dengan mudah diakses oleh setiap orang. Hingga kini teknologi informasi pun menawarkan berbagai kemudahan bagi penggunanya. Maka dengan itu pula pengguna teknologi ini pun mengalami peningkatan secara pesat. Kian bertambahnya pengguna teknologi informasi dapat mengakibatkan meningkatnya berbagai tindak kejahatan dalam penggunaan teknologi informasi itu sendiri.

Pada suatu sistem jaringan, arus komunikasi data dan keamanan informasi merupakan hal pokok yang harus dijaga. Informasi penting yang dikirimkan melalui jaringan beresiko mengalami penyadapan dan bahkan pengubahan data yang sering dilakukan oleh orang-orang yang tidak bertanggung jawab. Oleh karena itu, untuk menghindari hal tersebut, kita harus melakukan pencegahan dan pengamanan agar dapat mengurangi gangguan terhadap keamanan informasi pada arus komunikasi data dalam sistem jaringan.

Salah satu cara yang dapat dilakukan untuk menjaga kerahasiaan data dan keamanan informasi pada jaringan adalah dengan melakukan teknik ekripsi. Enkripsi adalah proses mengamankan suatu informasi dengan cara mengubah informasi asli (disebut dengan plaintext) menjadi informasi yang terenkripsi (disebut dengan chipertext) dengan menggunakan kunci pada operasi algoritma tertentu, sehingga informasi asli tersebut tidak dapat diketahui secara langsung oleh pihak lain. Berkebalikan dengan proses enkripsi, proses dekripsi digunakan untuk mengembalikan informasi yang terenkripsi (chipertext) menjadi informasi asli (plaintext).

Terdapat banyak algoritma yang dapat digunakan sebagai metode enkripsi dan dekripsi, salah satunya adalah algoritma Data Encryption Standard (DES) dengan menggunakan mode operasi Counter (CTR).

## Dasar Teori
### Data Encryption Standard
Pada bidang kriptografi, Data Encryption Standard (DES) adalah algoritma enkripsi kunci simetrik dan tergolong dalam jenis block cipher. Algoritma ini digunakan untuk mengenkripsi suatu blok plaintext berukuran 64-bit menjadi ciphertext berukuran 64-bit dengan menggunakan kunci yang berukuran 56-bit.

<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/24416774/151755e4-1410-11e7-9915-ef648ed8ac24.png" /></p>

### Counter
Counter (CTR) merupakan salah satu mode operasi yang digunakan untuk mengubah block cipher menjadi stream chipher. Mode operasi ini menghasilkan blok keystream selanjutnya dengan mengenkripsi nilai berkelanjutan dari suatu “counter”. Counter tersebut dapat berupa fungsi apapun yang mengeluarkan suatu sekuens yang menjamin tidak akan berulang dalam jangka waktu panjang. Meskipun demikian, jenis counter biasa (1, 2, 3, … dan seterusnya) lebih mudah dan sering digunakan. Mode Counter (CTR) sangat cocok untuk dioperasikan pada komputer multi-processor, dimana blok dapat diekripsikan secara pararel. Selain itu, mode ini juga tidak mengalami permasalahan short-cycle.

<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/24415268/1a5550ba-140b-11e7-92da-d8b3fa384ab9.png" /></p>

<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/24416039/99f93a82-140d-11e7-8e2f-946ffdec317d.png" /></p>

## Langkah Implementasi
### Langkah Pada Data Encryption Standard (DES)
1. Generate Subkeys <br/>
1.1 Memasukkan key yang ingin digunakan. Key ini akan sama dengan key yang akan digunakan untuk proses decryption.
Key juga jumlahnya harus tepat 64 bit <br/>
1.2 Key akan dipermutasi dengan menjadi 56 bit <br/>
1.3 Key akan dibagi dua menjadi C0 (28 bit pertama) dan D0 (28 bit terakhir) <br/>
1.4 Setiap C0 dan Do di shift ke kiri menjadi C1 dan D1. C1D1 akan menjadi subkey ke-1 atau K1 <br/>
1.5 Lakukan langkah 1.4 hingga didapatkan K16 <br/>

2. Generate Chiper Text <br/>
2.1 Message yang ingin dienkripsi kan dilakukan permutasi awal (Initiate Permutation)
2.2 Setalah itu, binary yang didapatkan akan dibagi dua menjadi L0 (32 bit pertama) dan R0 (32 bit terakhir) <br/>
2.3 Lalu dilakukan iterasi 16 kali dengan ketentuan L1 = R0 dan R1 = L0 = f(Ro, K1) (Rincian rumus ini akan <br/>
dilampirkan kemudian) <br/>
2.4 Hasil iterasi ke-16 adalah L16 dan R16 yang kemudian digabungkan <br/>
2.5 L16+R16 adalah hasil akhir dari chiper text <br/>

### Langkah implementasi pada DES dengan algoritma Counter
Berikut ini merupakan langkah implementasi algoritma Data Encryption Standard (DES) dengan menggunakan mode operasi Counter (CTR):
1. Enkripsi <br/>
1.1 CTR menggunakan counter dan key sebagai input pada algoritma DES <br/>
1.2 Counter adalah bilangan binary 64bit terurut yang terus di-increment per 64bit message yang dienkripsi
(Perhatikan diagram CTR di atas) <br/>
1.3 Ouput dari DES akan di XOR dengan message yang ingin dienkripsi <br/>
1.4 hasil dari XOR akan menghasilkan chiper text <br/>

2. Dekripsi <br/>
2.1. Lakukan langkah 1.1 dan 1.2 <br/>
2.2 Output dari DES akan di XOR dengan chiper text yang ingin didekripsi <br/>
2.3. Hasil dari XOR akan menghasilkan plain text <br/>

## Kesimpulan

## Saran
1. Semua implementasi algoritma yang kami buat menggunakan format string sekalipun format yang sedang dikerjakan
adalah binary atau string. Cara ini jauh lebih cepat dibandingkan diimplementasikan dalam bentuk List
2. Time consuming bisa lebih dipangkas jika format data benar-benar menggunakan Binary atau Hex
3. Implementasi dengan bahasa C/C++ akan jauh lebih cepat dari Python. Hanya saja Python akan jauh lebih mudah
4. Ada library Crypto pada Python. Tanpa harus membangun program sendiri, Python mempunyai library untuk DES
5. Output berupa HEX lebih manusiawi dibandingkan STRING.

## Terima Kasih

## Referensi
http://page.math.tu-berlin.de/~kant/teaching/hess/krypto-ws2006/des.htm
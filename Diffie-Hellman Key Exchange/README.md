# KIJ-F07
Tugas 3 - Implementasi Metode Diffie-Hellman Key Exchange pada algoritma Data Encryption Standard (DES) dengan menggunakan mode operasi Counter (CTR)

Kelompok F07 :
- Lucha Kamala P. (5114100062)
- Irfan Hanif     (5114100177)

## Pendahuluan
Pada arus komunikasi dalam jaringan, beberapa komputer dapat mengirimkan pesan antara satu sama lain. Pesan yang dikirimkan merupakan informasi penting yang harus dijaga agar tidak dapat diketahui oleh orang lain yang tidak bertanggung jawab. Tindak kejahatan yang sering terjadi dalam penggunaan teknologi informasi kian hari kian meningkat. Dalam komunikasi antar jaringan, pesan yang dikirimkan antar komputer beresiko mengalami penyadapan dan bahkan pengubahan data sehingga dapat merugikan pengguna teknologi informasi tersebut. Oleh karena itu, untuk menghindari hal tersebut, kita harus melakukan pencegahan dan pengamanan informasi agar dapat mengurangi gangguan terhadap keamanan informasi pada arus komunikasi data dalam sistem jaringan.

Salah satu metode yang dapat dilakukan untuk menjaga kerahasiaan data dan keamanan informasi jaringan adalah dengan menggunakan teknik enkripsi yaitu algoritma Data Encryption Standard (DES) dengan menggunakan mode operasi Counter (CTR). Algoritma ini digunakan untuk mengenkripsi dan mendekripsikan pesan text yang dikirimkan antar komputer. Komputer pertama akan melakukan enkripsi pesan, yaitu mengubah informasi asli (disebut dengan plaintext) menjadi informasi yang terenkripsi (disebut dengan ciphertext) dengan menggunakan kunci pada operasi algoritma tertentu, dan komputer lainnya akan melakukan dekripsi pesan yang telah diterima sehingga didapatkan pesan aslinya kembali.

Agar komputer penerima mampu untuk melakukan dekripsi pesan, maka kunci juga dikirimkan melalui lalu lintas jaringan. Untuk mengamankan kunci dari resiko penyadapan, maka digunakanlah metode Diffie-Hellman Key Exchange untuk menetapkan kunci secara bersama dan mengamankan kunci yang dikirimkan antar komputer. Dengan menggunakan metode ini, pesan dan kunci yang dikirimkan melalui lalu lintas jaringan menjadi aman dan terhindar dari resiko penyadapan serta tindak kejahatan teknologi informasi.

## Dasar Teori
### Sniffer
Sniffer adalah teknik pencurian dan penyadapan data informasi yang dilakukan dengan cara memonitoring atau melakukan analisis terhadap paket data yang dikirimkan antar komputer, yaitu dari komputer 1 ke komputer lainnya. Tools yang dapat digunakan untuk melakukan teknik sniffing adalah seperti Wireshark dan Netcut. Teknik sniffing ini dilakukan oleh para hacker atau penyusup yang berbahaya untuk melakukan tindakan yang dilarang seperti mencuri password dan data-data penting lainnya.

<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/24893869/935763cc-1eb0-11e7-8537-525c83bdb816.jpg" /></p>

### Diffie-Hellman Key Exchange
Diffie-Hellman Key Exchange adalah suatu metode yang digunakan dalam bidang kriptografi untuk mengamankan pertukaran kunci yang terjadi diantara 2 komputer. Pada komunikasi antar komputer, pesan terenkripsi antara kedua komputer menggunakan kunci yang telah ditetapkan sebelumnya. Dengan menggunakan metode Diffie-Hellman Key Exchange ini memungkinkan agar kedua komputer yang tidak memiliki pengetahuan sebelumnya dapat membuat kunci secara bersama-sama. Kunci ini kemudian dapat digunakan untuk mengenkripsi pesan yang dikirimkan. Parameter yang digunakan yaitu variabel a, yang hanya diketahui oleh komputer pertama, sedangkan komputer kedua tidak mengetahui. Begitu pula sebaliknya, variabel b hanya diketahui oleh komputer kedua, sedangkan komputer pertama tidak mengetahui. Dengan menggunakan metode ini, penyadap tidak akan bisa mengetahui kunci yang digunakan oleh 2 komputer.

<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25417308/6455e67a-2a6d-11e7-9fdd-0197da82e7f0.png" /></p>
<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25383558/e11ae4e4-29e6-11e7-9881-1b1b1b9c3006.png" /></p>

## Langkah Implementasi
### Langkah Implementasi metode Diffie-Hellman Key Exchange
Berikut ini merupakan langkah implementasi metode Diffie-Hellman Key Exchange pada algoritma Data Encryption Standard (DES) dengan menggunakan mode operasi Counter (CTR): <br/>
1. Membuat konfigurasi. <br/>
<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25514538/f19e234e-2c07-11e7-9a99-2fdd890259ae.png" /></p>
<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25514548/019009fc-2c08-11e7-91c6-07f10e5f5c3f.png" /></p>
2. Memanggil fungsi DiffieHellman. <br/>
<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25514564/1a6c0cbe-2c08-11e7-8f5e-e8337824724d.png" /></p>
3. Pada fungsi DiffieHellman, menentukan variabel P, yaitu bilangan prima yang besar, dan menentukan variabel G, yaitu generator, untuk disepakati bersama. <br/>
<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25514580/2c03cf5c-2c08-11e7-8e67-26cc9c7f7100.png" /></p>
4. Server membuka socket dan koneksi. <br/>
<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25514602/50cc11d2-2c08-11e7-838a-08ce57621132.png" /></p>
5. Client mendaftarkan koneksi dengan server. <br/>
<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25514614/6e5788a8-2c08-11e7-960d-856c49bea25e.png" /></p>
6. Setelah client terkoneksi dengan server, thread dijalankan. <br/>
<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25514660/b41ac760-2c08-11e7-8266-91327b5e617e.png" /></p>
<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25514677/c7bf2978-2c08-11e7-9081-787a2331de71.png" /></p>
7. Menentukan menentukan angka random rahasia secara berbeda. Angka ini kemudian disimpan sebagai variabel a bagi komputer pertama dan variabel b bagi komputer kedua. <br/>
<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25514703/e790dcc4-2c08-11e7-9dd8-c2d74fb879fe.png" /></p>
<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25514715/f86734da-2c08-11e7-8ade-07b1463a4f80.png" /></p>
8. Masukkan variabel-variabel yang telah ditentukan ke dalam fungsi DiffieHellman untuk mendapatkan nilai public_number, yaitu variabel A bagi komputer pertama dan variabel B bagi komputer kedua. Kemudian nilai public_number ini akan dikirimkan antara satu sama lain. <br/> 
<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25514726/09b83b12-2c09-11e7-9b20-f2e8019fb6c6.png" /></p>
9. Melakukan perhitungan dengan nilai public_number yang telah diterima untuk membuat kunci. Dari hasil perhitungan ini akan didapatkan kunci yang sama untuk digunakan dalam melakukan proses enkripsi dan dekripsi pesan. <br/>
<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25514734/218270b4-2c09-11e7-883b-6a3b6e7bd7c8.png" /></p>
10. Thread yang dijalankan akan menjalankan 2 proses pada client dan server, yaitu proses pengiriman dan proses penerimaan.<br/>
Proses pengiriman pada server :
<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25514803/aede6a4e-2c09-11e7-98e2-1f1b62f66e80.png" /></p>
Proses penerimaan oleh server :
<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25514824/da2366a0-2c09-11e7-98ef-455a6c907536.png" /></p>
Proses pengiriman pada client :
<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25514841/f65b8ac8-2c09-11e7-85b2-3e133b164ab5.png" /></p>
Proses penerimaan oleh client :
<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25514859/12ec7fee-2c0a-11e7-98ae-f211ca741f40.png" /></p>

## Input dan Output Program
1. Masukkan username sebagai komputer 1. <br/>
<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25515020/d2d2bab6-2c0b-11e7-91e9-ed25852add76.png" /></p>
2. Masukkan username sebagai komputer 2. <br/>
<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25515027/e1702c16-2c0b-11e7-851f-acb5fca3aa28.png" /></p>
3. Masukkan pesan yang ingin dikirimkan antar komputer. <br/>
<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25515038/f3ef6802-2c0b-11e7-8fa2-ab49499b238d.png" /></p>
4. Komputer 2 akan menerima pesan yang telah dikirimkan oleh komputer 1. <br/>
<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25515048/0939e71e-2c0c-11e7-80b9-a42448da7b89.png" /></p>
5. Komputer 2 juga dapat membalas dan mengirimkan pesan kepada komputer 1. <br/>
<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25515058/174433fa-2c0c-11e7-9c02-6c1e17893d19.png" /></p>
6. Komputer 1 akan menerima balasan pesan dari komputer 2.
<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25515069/2649051a-2c0c-11e7-8928-e8343d8241b2.png" /></p>

## Kesimpulan
Penerapan metode Diffie-Hellman Key Exchange pada algoritma Data Encryption Standard (DES) dengan menggunakan mode operasi Counter (CTR) dapat mengamankan kunci dan pesan yang dikirimkan dalam komunikasi antara 2 komputer dalam lalu lintas jaringan. Metode ini mampu untuk mengamankan kunci yang dikirimkan, sehingga pesan yang dikirimkan dalam lalu lintas jaringan menjadi sulit untuk dilakukan penyadapan (sniffer) karena penyadap tidak mampu untuk melakukan proses enkripsi dan dekripsi pesan tanpa mengetahui kunci yang digunakan.

## Saran
1. Semua implementasi algoritma yang kami buat menggunakan format string meskipun format yang sedang dikerjakan adalah binary atau string. Cara ini jauh lebih cepat dibandingkan bila diimplementasikan dalam bentuk List. <br/>
2. Waktu yang digunakan untuk proses dapat dipangkas apabila format data benar-benar menggunakan Binary atau Hex. <br/>
3. Implementasi dengan bahasa C/C++ akan jauh lebih cepat daripada bahasa Python. Hanya saja Python jauh lebih mudah. <br/>
4. Terdapat library Crypto pada Python. Tanpa harus membangun program sendiri, Python memiliki library untuk algoritma DES. <br/>
5. Output berupa HEX lebih mudah dipahami oleh pengguna dibandingkan output berupa STRING. <br/>

## Referensi
1. http://page.math.tu-berlin.de/~kant/teaching/hess/krypto-ws2006/des.htm <br/>
2. https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation <br/>
3. Final Project Pemrograman Jaringan milik Irfan pada semester 5 <br/>
4. https://en.wikipedia.org/wiki/Diffie–Hellman_key_exchange <br/>

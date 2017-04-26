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
Sniffer adalah teknik pencurian dan penyadapan data informasi yang dilakukan dengan cara memonitoring atau melakukan analisis terhadap paket data yang dikirimkan antar komputer, yaitu dari komputer client ke komputer server. Tools yang dapat digunakan untuk melakukan teknik sniffing adalah seperti Wireshark dan Netcut. Teknik sniffing ini dilakukan oleh para hacker atau penyusup yang berbahaya untuk melakukan tindakan yang dilarang seperti mencuri password dan data-data penting lainnya.

<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/24893869/935763cc-1eb0-11e7-8537-525c83bdb816.jpg" /></p>

### Diffie-Hellman Key Exchange
Diffie-Hellman Key Exchange adalah suatu metode yang digunakan dalam bidang kriptografi untuk mengamankan pertukaran kunci yang terjadi diantara 2 komputer. Pada komunikasi antar komputer, pesan terenkripsi antara kedua komputer menggunakan kunci yang telah ditetapkan sebelumnya. Dengan menggunakan metode Diffie-Hellman Key Exchange ini memungkinkan agar kedua komputer yang tidak memiliki pengetahuan sebelumnya dapat membuat kunci secara bersama-sama. Kunci ini kemudian dapat digunakan untuk mengenkripsi pesan yang dikirimkan. Parameter yang digunakan yaitu Xa, yang hanya diketahui oleh komputer pertama, sedangkan komputer kedua tidak mengetahui. Begitu pula sebaliknya, parameter Xb hanya diketahui oleh komputer kedua, sedangkan komputer pertama tidak mengetahui. Dengan menggunakan metode ini, penyadap tidak akan bisa mengetahui kunci yang digunakan oleh 2 komputer.

<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25417308/6455e67a-2a6d-11e7-9fdd-0197da82e7f0.png" /></p>

## Langkah Implementasi
### Langkah Implementasi metode Diffie-Hellman Key Exchange
<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25383558/e11ae4e4-29e6-11e7-9881-1b1b1b9c3006.png" /></p>
Berikut ini merupakan langkah implementasi metode Diffie-Hellman Key Exchange pada algoritma Data Encryption Standard (DES) dengan menggunakan mode operasi Counter (CTR): <br/>
1. Menentukan P, yaitu salah satu bilangan prima dan menentukan G, yaitu generator. <br/>
2. Komputer pertama dan komputer kedua menentukan angka random rahasia secara berbeda. Angka ini disimpan sebagai variabel a bagi komputer pertama dan variabel b bagi komputer kedua. <br/>
3. Masukkan angka yang telah ditentukan ke dalam rumus A = G^a mod P untuk komputer pertama dan B = G^b mod P untuk komputer kedua. <br/>
4. Hasil perhitungan dari langkah no. 3 dikirimkan antara satu sama lain. <br/>
5. Komputer akan melakukan perhitungan terhadap angka yang telah didapatkan untuk mendapatkan kunci. Komputer pertama akan menggunakan rumus yaitu K = B^a mod P dan komputer kedua akan menggunakan rumus K = A^b mod P. Dari hasil perhitungan tersebut akan didapatkan kunci yang sama untuk digunakan dalam melakukan enkripsi dan dekripsi pesan. <br/>

## Teknik Operasi
Berikut ini merupakan beberapa teknik operasi yang digunakan dalam implementasi algoritma Data Encryption Standard (DES) dengan menggunakan mode operasi Counter (CTR):
### Permutasi
Permutasi adalah teknik operasi yang digunakan untuk menyusun urutan input biner dalam urutan yang berbeda dari urutan semula sesuai dengan urutan pada tabel mutlak atau statis yang telah ditetapkan. </br>
Contoh: </br>
Input biner &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;0&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;0 </br>
Index ke- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [0][1][2][3][4] </br>
Urutan index pada tabel mutlak/statis &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [4][0][3][1][2] </br>
Hasil permutasi &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;0 </br>

### Left Shift
Left Shift adalah teknik operasi yang digunakan untuk melakukan pergeseran urutan input biner ke arah kiri sebanyak nilai pergeseran yang telah ditetapkan pada tabel mutlak atau statis. </br>
Contoh: </br>
Input biner&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1  1  0  1  0 </br>
Jumlah pergeran pada tabel multak/statis [1, 2, 2, 1, ... dst] </br>
Hasil iterasi ke-0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1  0  1  0  1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(digeser sebanyak 1 kali ke kiri) </br>
Hasil iterasi ke-1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1  0  1  1  0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(digeser sebanyak 2 kali ke kiri) </br>
Hasil iterasi ke-2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1  1  0  1  0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(digeser sebanyak 2 kali ke kiri) </br>
Hasil iterasi ke-3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1  0  1  0  1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(digeser sebanyak 1 kali ke kiri) </br>
dan seterusnya .... </br>

### XOR
XOR (Exclusive OR) adalah teknik operasi yang digunakan untuk menghasilkan angka biner yaitu 0 atau 1. Teknik operasi ini akan menghasilkan keluaran angka biner 0 apabila kedua inputan sama, dan menghasilkan keluaran angka biner 1 apabila kedua inputan berbeda. </br> 
Contoh: </br>
Input biner 1 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  1  1  0  1  0 </br>
Input biner 2 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  1  0  1  1  1 </br>
Hasil XOR &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0  1  1  0  1 </br>

### S-Box
S-Box (Substitution-Box) adalah teknik operasi yang digunakan untuk menggantikan nilai input biner menjadi nilai biner pada state yang ditunjuk pada tabel mutlak atau statis. Nilai baris yang ditunjuk merupakan gabungan nilai input biner bit pertama dan bit terakhir. Sisanya merupakan nilai kolom yang ditunjuk. </br>
Contoh: </br>
Input biner&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 0 1 1 0 1 </br>
menunjuk pada baris ke- &nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp; (11 yaitu baris ke-3) </br>
menunjuk pada kolom ke- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0&nbsp;1&nbsp;1&nbsp;0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (0110 yaitu kolom ke-6) </br>
Berdasarkan baris ke-3 kolom ke-6 yang ditunjuk pada tabel mutlak atau statis didapatkan nilai biner yaitu 1 atau 0001.

## Input dan Output Program
### Input Program
Masukkan key yang ingin digunakan dan message yang ingin dikirimkan pada side client. Berikut ini merupakan input program: <br/>
Key : irfan <br/>
Message : Halo Lucha <br/>

<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/24913777/65893334-1efc-11e7-8a64-b93b39236ad2.png" /></p>

### Output Program
Output program berupa hasil enkripsi yaitu message yang telah diekripsikan (ciphertext) dan hasil dekripsi yaitu message asli (plaintext) pada side server. Berikut ini merupakan output program pada side server:

<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/24914133/87631fb4-1efd-11e7-8f4c-53cfc15bd1f1.png" /></p>

Message yang telah diterima server, kemudian akan dikirimkan ulang oleh server kepada client. Berikut ini merupakan output program pada side client:

<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/24913807/8610e868-1efc-11e7-9c3d-d9f85ac73ef0.png" /></p>

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
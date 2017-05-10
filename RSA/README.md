# KIJ-F07
Tugas 4 - Implementasi Algoritma RSA pada Proses Enkripsi dan Dekripsi Pesan

Kelompok F07 :
- Lucha Kamala P. (5114100062)
- Irfan Hanif     (5114100177)

## Pendahuluan
Seiring dengan pesatnya perkembangan teknologi informasi, informasi dapat dengan mudah diakses oleh setiap orang. Pada saat ini, teknologi informasi telah menawarkan berbagai kemudahan bagi penggunanya. Oleh karena itu, maka pengguna teknologi ini pun mengalami peningkatan secara pesat setiap tahunnya. Kian bertambahnya pengguna teknologi informasi dapat mengakibatkan meningkatnya berbagai tindak kejahatan yang terjadi dalam penggunaan teknologi informasi.

Pada arus komunikasi dalam jaringan, beberapa komputer dapat mengirimkan pesan antara satu sama lain. Pesan yang dikirimkan merupakan informasi penting yang harus dijaga agar tidak sampai diketahui oleh orang lain. Pertukaran pesan yang dikirimkan antar komputer ini beresiko mengalami penyadapan dan bahkan pengubahan data yang dapat dilakukan oleh orang-orang yang tidak bertanggung jawab, sehingga dapat menyebabkan kerugikan bagi pengguna teknologi informasi tersebut. Oleh karena itu, untuk menghindari hal ini, maka kita harus melakukan pencegahan dan pengamanan data informasi agar dapat mengurangi gangguan terhadap keamanan informasi pada arus komunikasi data dalam suatu sistem jaringan.

Salah satu cara yang dapat dilakukan untuk menjaga kerahasiaan data dan keamanan informasi jaringan adalah dengan menggunakan metode enkripsi dan dekripsi pesan. Enkripsi adalah proses mengamankan suatu informasi dengan cara mengubah informasi asli (disebut dengan plaintext) menjadi informasi yang terenkripsi (disebut dengan ciphertext) dengan menggunakan kunci pada operasi algoritma tertentu, sehingga informasi asli tersebut tidak dapat diketahui secara langsung oleh pihak lain. Berkebalikan dengan proses enkripsi, proses dekripsi digunakan untuk mengembalikan informasi yang telah terenkripsi (ciphertext) menjadi informasi asli (plaintext).

Terdapat beberapa algoritma yang dapat digunakan sebagai metode enkripsi dan dekripsi pesan, salah satunya yaitu algoritma RSA. Algoritma ini digunakan untuk mengenkripsi dan mendekripsikan pesan text yang dikirimkan antar komputer. Komputer Pengirim akan melakukan enkripsi pesan. Komputer Penerima akan membuat 2 kunci, yaitu public key dan private key. Public key akan dikirimkan ke komputer Pengirim untuk digunakan sebagai kunci untuk melakukan proses enkripsi. Setelah melakukan proses enkripsi, Komputer Pengirim akan mengirimkan pesan terenkripsi ke Komputer Penerima. Komputer Penerima akan melakukan proses dekripsi pesan yang telah diterima dengan menggunakan private key yang dimiliki sehingga didapatkan pesan aslinya kembali. Dengan menggunakan algoritma RSA ini, maka pesan yang dikirimkan melalui lalu lintas jaringan menjadi aman dan terhindar dari resiko penyadapan serta tindak kejahatan teknologi informasi.

## Dasar Teori
### Client-Server
Dalam komunikasi antar komputer pada lalu lintas jaringan, client adalah pihak yang menerima dan menampilkan serta menjalankan aplikasi (software komputer). Server adalah pihak yang menyediakan dan bertindak sebagai pengelola aplikasi, data, dan keamanannya. Sedangkan pesan merupakan data informasi text yang dikirim atau disampaikan antara pihak client dan pihak server.

<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/24907211/773fe0e4-1ee5-11e7-91b6-3627b749f076.png" /></p>

### Sniffer
Sniffer adalah teknik pencurian dan penyadapan data informasi yang dilakukan dengan cara memonitoring atau melakukan analisis terhadap paket data yang dikirimkan antar komputer, yaitu dari komputer 1 ke komputer lainnya. Tools yang dapat digunakan untuk melakukan teknik sniffing adalah seperti Wireshark dan Netcut. Teknik sniffing ini dilakukan oleh para hacker atau penyusup yang berbahaya untuk melakukan tindakan yang dilarang seperti mencuri password dan data-data penting lainnya.

<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/24893869/935763cc-1eb0-11e7-8537-525c83bdb816.jpg" /></p>

### RSA
Pada bidang kriptografi, RSA adalah algoritma yang digunakan oleh komputer modern untuk melakukan proses enkripsi dan dekripsi pesan. RSA merupakan singkatan dari inisial nama penemu algoritma ini, yaitu Rivest-Shamir-Adleman. Algoritma ini termasuk dalam jenis algoritma kriptografi asimetrik, karena terdapat 2 kunci yang berbeda, dan juga sering disebut sebagai algoritma kriptografi public key, karena salah satu kuncinya dapat diberikan kepada semua orang (public key) sedangkan kunci yang satunya harus tetap dijaga kerahasiaannya (private key).

Algoritma RSA berdasarkan fakta bahwa menemukan faktor bilangan bulat adalah cukup sulit. Pengguna algoritma ini harus menentukan 2 bilangan prima yang cukup besar untuk dijadikan sebagai nilai public key dan private key. Bilangan prima yang telah ditentukan sebagai nilai private key harus dirahasiakan. Siapapun dapat menggunakan nilai public key yang telah ditentukan untuk melakukan enkripsi pesan. Apabila nilai public key cukup besar, maka hanya seseorang yang mengetahui nilai private key tersebut yang dapat melakukan dekripsi pesan dan memecahkan kode pesan yang dikirimkan.

RSA merupakan algoritma pertama yang cocok untuk digital signature dan merupakan salah satu algoritma yang paling maju dalam bidang kriptografi puclic key. Algoritma RSA masih digunakan secara luas hingga saat ini dan dipercaya mampu untuk mengamankan informasi dengan menggunakan kunci yang cukup panjang.

<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25848866/7480c55a-34e6-11e7-8ad0-b2c48543928e.gif" /></p>
<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25848899/9176a9c2-34e6-11e7-9cfe-c6c34cbbe177.jpg" /></p>
<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25848912/9e165f38-34e6-11e7-92b3-c0decbbe0f4a.jpg" /></p>
<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25848928/b0d7af28-34e6-11e7-8892-04ef0b9dc28d.jpg" /></p>

## Langkah Implementasi
### Langkah Implementasi algoritma RSA
Berikut ini merupakan langkah implementasi algoritma RSA: <br/>
##### A. Proses Pembuatan Kunci
1. Menentukan 2 bilangan prima yang berbeda secara random dan bernilai besar untuk kemudian disimpan sebagai variabel p dan q. Untuk mendapatkan bilangan prima secara random, maka digunakan fungsi MillerRabin.

<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25893993/563a688a-35a4-11e7-81dc-d5369eed568c.png" /></p>
<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25894058/96504688-35a4-11e7-83e4-b8bc21f55852.png" /></p>
<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25894020/6f017836-35a4-11e7-8879-ab085375e3be.png" /></p>
<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25894037/81dcbbe6-35a4-11e7-9f27-addf52aeb5af.png" /></p>

2. Menghitung nilai n = p*q.

<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25894071/a9dd88f0-35a4-11e7-808f-d7e1c4205ca2.png" /></p>

3. Mengitung nilai totient, yaitu m = (p-1)*(q-1).

<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25894103/cb4e4542-35a4-11e7-9dea-e1712ffde218.png" /></p>

4. Menentukan bilangan bulat yang kemudian akan disimpan sebagai variabel e, yaitu antara 1 hingga m (1 < e < m), dimana variabel e juga merupakan ko-prima dari m.

<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25894124/deb89380-35a4-11e7-83e7-1ef58d44c1ee.png" /></p>

5. Menghitung nilai d = e^-1 (mod m) dengan menggunakan Extended Euclidean Algorithm.

<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25894156/fd4cf368-35a4-11e7-8afd-4cbc506c69d0.png" /></p>
<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25894200/1f8958ea-35a5-11e7-9230-c049434ae94b.png" /></p>

6. Public key adalah {e, n}.

<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25894227/3c94460c-35a5-11e7-8a23-e97384730b10.png" /></p>

7. Private key adalah {d, n}.

<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25894253/5284c9fa-35a5-11e7-9d3f-40dd8857f2bb.png" /></p>

##### C. Proses Enkripsi Pesan
1. Memasukkan pesan.

<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25894306/7affdabe-35a5-11e7-9984-e1d44f7c9823.png" /></p>

2. Mengubah karakter pesan menjadi kode ASCII kemudian melakukan enkripsi dengan menggunakan fungsi enkripsi yaitu c = m^e mod n. Proses enkripsi dilakukan dengan menggunakan public key yaitu {e, n}.

<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25894345/9cc23278-35a5-11e7-9a45-457c5ae8c77b.png" /></p>

##### D. Proses Dekripsi Pesan
1. Menerima pesan terenkripsi.

<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25894393/d1a85698-35a5-11e7-8c5c-8ce385c0c236.png" /></p>

2. Melakukan dekripsi dengan menggunakan fungsi dekripsi yaitu m = c^d mod n. Proses dekripsi dilakukan dengan menggunakan private key yaitu {d, n}.

<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25894428/f2a7b67c-35a5-11e7-804b-534a923cdc0a.png" /></p>

## Input dan Output Program
1. Komputer 1 memasukkan pesan yang ingin dikirimkan. <br/>

<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25895527/813ab3fe-35aa-11e7-9d96-4749ca71b758.png" /></p>

2. Komputer 2 akan menerima pesan dari komputer 1. <br/>

<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25895553/924dfc64-35aa-11e7-8c54-04d3650603eb.png" /></p>

3. Komputer 2 dapat membalas pesan. <br/>

<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25895570/a3909aa4-35aa-11e7-8975-cd32eab03ac3.png" /></p>

4. Komputer 1 akan menerima pesan balasan dari komputer 2. <br/>

<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/25895580/b20e2344-35aa-11e7-873b-429009a6af03.png" /></p>

## Kesimpulan
Implementasi algoritma RSA pada proses enkripsi dan dekripsi pesan dapat mengamankan pesan dan public key yang dikirimkan dalam komunikasi antara 2 komputer dalam lalu lintas jaringan. Algoritma ini mampu untuk mengamankan pesan yang dikirimkan, sehingga pesan terenkripsi yang dikirimkan dalam lalu lintas jaringan menjadi sulit untuk dilakukan penyadapan (sniffer) karena penyadap tidak mampu untuk melakukan proses dekripsi pesan tanpa mengetahui private key yang digunakan.

## Saran
1. Semua implementasi algoritma yang kami buat menggunakan format string meskipun format yang sedang dikerjakan adalah binary atau string. Cara ini jauh lebih cepat dibandingkan bila diimplementasikan dalam bentuk List. <br/>
2. Waktu yang digunakan untuk proses dapat dipangkas apabila format data benar-benar menggunakan Binary atau Hex. <br/>
3. Implementasi dengan bahasa C/C++ akan jauh lebih cepat daripada bahasa Python. Hanya saja Python jauh lebih mudah. <br/>
4. Terdapat library Crypto pada Python. Tanpa harus membangun program sendiri, Python memiliki library untuk algoritma RSA. <br/>
5. Output berupa HEX lebih mudah dipahami oleh pengguna dibandingkan output berupa STRING. <br/>

## Referensi
1. Final Project Pemrograman Jaringan milik Irfan pada semester 5 <br/>
2. http://octarapribadi.blogspot.co.id/2016/02/enkripsi-dan-dekripsi-menggunakan-rsa.html <br/>
3. https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm <br/>
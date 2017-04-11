# KIJ-F07
Tugas 1 - Implementasi algoritma Data Encryption Standard (DES) dengan menggunakan mode operasi Counter (CTR)

Kelompok F07 :
- Lucha Kamala P. (5114100062)
- Irfan Hanif     (5114100177)

## Pendahuluan
Seiring dengan perkembangan teknologi informasi secara pesat, informasi dapat dengan mudah diakses oleh setiap orang. Hingga kini teknologi informasi pun menawarkan berbagai kemudahan bagi penggunanya. Maka dengan itu pula pengguna teknologi ini pun mengalami peningkatan secara pesat. Kian bertambahnya pengguna teknologi informasi dapat mengakibatkan meningkatnya berbagai tindak kejahatan dalam penggunaan teknologi informasi itu sendiri.

Pada suatu sistem jaringan, arus komunikasi data dan keamanan informasi merupakan hal pokok yang harus dijaga. Informasi penting yang dikirimkan melalui jaringan beresiko mengalami penyadapan dan bahkan pengubahan data yang sering dilakukan oleh orang-orang yang tidak bertanggung jawab. Oleh karena itu, untuk menghindari hal tersebut, kita harus melakukan pencegahan dan pengamanan agar dapat mengurangi gangguan terhadap keamanan informasi pada arus komunikasi data dalam sistem jaringan.

Salah satu cara yang dapat dilakukan untuk menjaga kerahasiaan data dan keamanan informasi pada jaringan adalah dengan melakukan teknik enkripsi. Enkripsi adalah proses mengamankan suatu informasi dengan cara mengubah informasi asli (disebut dengan plaintext) menjadi informasi yang terenkripsi (disebut dengan ciphertext) dengan menggunakan kunci pada operasi algoritma tertentu, sehingga informasi asli tersebut tidak dapat diketahui secara langsung oleh pihak lain. Berkebalikan dengan proses enkripsi, proses dekripsi digunakan untuk mengembalikan informasi yang terenkripsi (ciphertext) menjadi informasi asli (plaintext).

Terdapat banyak algoritma yang dapat digunakan sebagai metode enkripsi dan dekripsi, salah satunya adalah algoritma Data Encryption Standard (DES) dengan menggunakan mode operasi Counter (CTR).

## Dasar Teori
### Data Encryption Standard
Pada bidang kriptografi, Data Encryption Standard (DES) adalah algoritma enkripsi kunci simetrik dan tergolong dalam jenis block cipher. Algoritma ini digunakan untuk mengenkripsi suatu blok plaintext berukuran 64-bit menjadi ciphertext berukuran 64-bit dengan menggunakan kunci yang berukuran 56-bit.

<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/24416774/151755e4-1410-11e7-9915-ef648ed8ac24.png" /></p>

### Counter
Counter (CTR) merupakan salah satu mode operasi yang digunakan untuk mengubah block cipher menjadi stream cipher. Mode operasi ini menghasilkan blok keystream selanjutnya dengan mengenkripsi nilai berkelanjutan dari suatu “counter”. Counter tersebut dapat berupa fungsi apapun yang mengeluarkan suatu sekuens yang menjamin tidak akan berulang dalam jangka waktu panjang. Meskipun demikian, jenis counter biasa (1, 2, 3, … dan seterusnya) lebih mudah dan sering digunakan. Mode Counter (CTR) sangat cocok untuk dioperasikan pada komputer multi-processor, dimana blok dapat diekripsikan secara pararel. Selain itu, mode ini juga tidak mengalami permasalahan short-cycle.

<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/24415268/1a5550ba-140b-11e7-92da-d8b3fa384ab9.png" /></p>

<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/24416039/99f93a82-140d-11e7-8e2f-946ffdec317d.png" /></p>

## Langkah Implementasi
### Langkah Implementasi Algoritma Data Encryption Standard (DES)
Berikut ini merupakan langkah implementasi algoritma Data Encryption Standard (DES):
1. Generate Subkeys <br/>
1.1 Memasukkan key yang ingin digunakan. Key ini akan sama dengan key yang akan digunakan untuk proses dekripsi. Jumlah key harus tepat sebanyak 64-bit. <br/>
1.2 Key akan dipermutasi menjadi 56-bit. <br/>
1.3 Key akan dibagi menjadi dua bagian, yaitu C0 (28-bit pertama) dan D0 (28-bit terakhir). <br/>
1.4 Setiap C0 dan D0 digeser ke kiri menjadi C1 dan D1. C1D1 akan menjadi subkey ke-1 atau K1. <br/>
1.5 Lakukan langkah 1.4 secara berulang hingga didapatkan subkey ke-16 atau K16. <br/>

2. Generate Ciphertext <br/>
2.1 Message yang ingin dienkripsikan dilakukan permutasi awal (Initiate Permutation). <br/>
2.2 Setelah itu, binary yang didapatkan akan dibagi menjadi dua bagian, yaitu L0 (32-bit pertama) dan R0 (32-bit terakhir). <br/>
2.3 Kemudian lakukan iterasi sebanyak 16 kali dengan ketentuan L1=R0 dan R1=L0=f(Ro,K1). (Rincian rumus ini akan dilampirkan kemudian) <br/>
2.4 Hasil iterasi ke-16 adalah L16 dan R16 yang kemudian digabungkan. <br/>
2.5 L16+R16 adalah hasil akhir dari ciphertext. <br/>

### Langkah Implementasi Algoritma DES dengan Menggunakan Mode Operasi Counter (CTR)
Berikut ini merupakan langkah implementasi algoritma Data Encryption Standard (DES) dengan menggunakan mode operasi Counter (CTR):
1. Enkripsi <br/>
1.1 Mode operasi Counter (CTR) menggunakan counter dan key sebagai input pada algoritma DES. <br/>
1.2 Counter adalah bilangan binary 64-bit terurut yang terus dilaukan increment per 64-bit message yang dienkripsi. (Perhatikan diagram Enkripsi Counter (CTR) di atas) <br/>
1.3 Output dari algoritma DES akan di XOR dengan message yang ingin dienkripsi. <br/>
1.4 Hasil dari XOR akan menghasilkan ciphertext. <br/>

2. Dekripsi <br/>
2.1 Lakukan langkah 1.1 dan 1.2. <br/>
2.2 Output dari algoritma DES akan di XOR dengan ciphertext yang ingin didekripsi. <br/>
2.3 Hasil dari XOR akan menghasilkan plaintext. <br/>

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
### Testcase 1
Masukkan key yang ingin digunakan dan message yang ingin dienkripsikan sebagai input program. Berikut ini merupakan input program: <br/>
Key : kij123 <br/>
Message : produk Smart City yang muncul karena seringnya terjadi banjir yang melanda <br/>

<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/24586846/56922324-17d4-11e7-8eaf-b63c5a73a2dd.png" /></p>

Output program berupa hasil enkripsi yaitu message yang telah diekripsikan (ciphertext) dan hasil dekripsi yaitu message asli (plaintext). Berikut ini merupakan output program:

<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/24586852/99c7ae52-17d4-11e7-9486-5b04ffd21b07.png" /></p>

### Testcase 2
Masukkan key yang ingin digunakan dan message yang ingin dienkripsikan sebagai input program. Berikut ini merupakan input program: <br/>
Key : lucirf12 <br/>
Message : Sensor ini bertujuan untuk memantau dan mengirimkan informasi air ke pemantau <br/>

<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/24586857/bb5f90d4-17d4-11e7-9bf3-26ebb6934b79.png" /></p>

Output program berupa hasil enkripsi yaitu message yang telah diekripsikan (ciphertext) dan hasil dekripsi yaitu message asli (plaintext). Berikut ini merupakan output program:

<p align="center"><img src="https://cloud.githubusercontent.com/assets/26644539/24586862/e347812e-17d4-11e7-99b6-fc06f6fa2c67.png" /></p>

## Kesimpulan
Mode operasi Counter (CTR) sangat well-designed karena dapat melakukan enkripsi-dekripsi secara dua arah (bolak-balik) hanya dengan algoritma enkripsi Data Encryption Standard (DES). Dengan distribusi key yang baik, maka algoritma ini dapat menjadi salah satu algoritma yang sangat kuat dan mudah untuk diimplementasikan.

## Saran
1. Semua implementasi algoritma yang kami buat menggunakan format string meskipun format yang sedang dikerjakan adalah binary atau string. Cara ini jauh lebih cepat dibandingkan bila diimplementasikan dalam bentuk List. <br/>
2. Waktu yang digunakan untuk proses dapat dipangkas apabila format data benar-benar menggunakan Binary atau Hex. <br/>
3. Implementasi dengan bahasa C/C++ akan jauh lebih cepat daripada bahasa Python. Hanya saja Python jauh lebih mudah. <br/>
4. Terdapat library Crypto pada Python. Tanpa harus membangun program sendiri, Python memiliki library untuk algoritma DES. <br/>
5. Output berupa HEX lebih mudah dipahami oleh pengguna dibandingkan output berupa STRING. <br/>

## Referensi
1. http://page.math.tu-berlin.de/~kant/teaching/hess/krypto-ws2006/des.htm <br/>
2. https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation <br/>

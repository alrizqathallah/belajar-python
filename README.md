# Python

## BAB 1: Pengenalan & Persiapan

### Bagian 1

**1. Tujuan Pembelajaran**
Fokus kita di tahap pertama ini adalah memahami esensi bahasa Python dan mengapa industri sangat menyukainya, sebelum kita menyiapkan perangkatnya.

**2. Penjelasan Konsep Utama: Apa itu Python?**
Python adalah bahasa pemrograman tingkat tinggi. Istilah "tingkat tinggi" berarti sintaksisnya (aturan penulisannya) dirancang agar sangat mudah dibaca oleh manusia, karena bentuknya mendekati bahasa inggris dasar.

**Visualisasi & Analogi**
Bayangkan kita sedang memberikan resep kepada seorang asisten koki (komputer) untuk membuat kue.
  * Jika menggunakan bahasa pemrograman tingkat rendah, kita harus menjelaskan instruksi mekanis yang sangat rumit: "Posisikan sendok pada koordinat x, y, lalu gerakkan melingkar dengan kecepatan 2 m/s."
  * Dengan bahasa tingkat tinggi seperti Python, kita cukup memberi instruksi sederahan: `aduk_adonan()`. Python memiliki "penerjemah" di belakang layar yang akan mengubah teks sederhana itu menjadi kode biner rumit yang dimengerti mesin.

**Study Kasus: Mengapa Python?**
Di dunia industri modern, efisiensi waktu adalah segalanya. Python digunakan oleh raksasa teknologi (seperti Google, Netflix dan Instagram) karena developer bisa menulis lebih sedikit baris kode untuk mencapai tujuan yang sama dibandingkan bahasa lain. Penggunaannya sangat luas: dari membangun sistem web (Backend), menganalisis jutaan baris data keuangan (Data Science), hingga melatih kecerdasan buatan (Machine Learning).

Sebelum kita melangkah ke proses instalasi Python dan Editor kodenya (seperti VS Code), mari kita bangun pola pikir pemecah masalah. Jika kita memiliki asisten pintas yang bisa diprogram untuk melakukan tugas berulang di komputer, apa yang pertama kali ingin kita otomatisasikan atau berikan kepadanya?

Untuk memberi sedikit gambaran, ini beberapa tugas yang sering diserahkan orang kepada Python agar mereka tidak perlu bekerja manual:
  * **Merapikan File**: Otomatis memilih ratusan file di folder "Downloads" yang berantakan (otomatis memindahkan gambar ke folder Gambar, dokumen ke folder Dokumen, dst).
  * **Mengambil Data**: Mengunduh daftar harga barang dari toko *online* setiap jam untuk mencari tahu kapan ada diskon termurah.
  * **Pesan Otomatis**: Mengirim pesan WhatsApp atau email ke 50 teman dengan menyebutkan nama mereka masing-masing tanpa harus *copy-paste* satu per satu.

Hal-hal seperti itulah yang akan perlahan kita pelajari cara membuatnya. Namun, sebelum asisten kita bisa bekerja, kita harus meyiapkan "alat kerjanya" terlebih dahulu di komputer kita.

### Bagian 2

**Penjelasan Konsep: Alat Kerja Python**
Untuk menulis dan menjalankan Python, kita secara umum membutuhkan dua hal:
  1.  **Python Interpreter (Penerjemahan)**: Ini adalah mesin utamanya. Komputer tidak mengerti bahasa Python, ia hanya mengerti angka 1 dan 0. Interpreter ini bertugas membaca tulisan Python kita, lalu menerjemahkannya menjadi 1 dan 0 secara *rela-time* agar komputer bisa menjalankannya.
  2.  **Code Editor (Penyunting Kode)**: Ini adalah "buku tulis" tempat kita merangkai kode. Kita sebenarnya bisa menulis kode Python di *Notepad*, tetapi itu akan sangat sulit. Kita akan menggunakan **Visual Studio Code (VS Code)**, editor gratis yang sangat populer di industri karena bisa memberi warna pada kode dan memberi tahu jika ada salah ketik (typo).

### Bagian 3

**Penjelasan Konsep Utama & Perisapan Lingkungan Kerja**

Karena kita menggunakan WSL Ubuntu, kemungkinan besar Python sudah terpasang otomatis. Di dunia Linux, Python adalah komponen penting yang digunakan oleh sistem itu sendiri.

**Langkah 1: Memeriksan Python di Terminal**
Buka terminal Ubuntu (bisa dicari di menu Start Windows dengan mengetik "Ubuntu"), lalu ketik perintah berikut dan tekan Enter:

```terminal
python3 --version
```

**Langkah 2: Menyiapkan VS Code dengan WSL**
  1.  Unduh dan instal **Visual Studio Code** di Windows seperti biasa.
  2.  Buka VS Code, klik ikon kotak-kotak di menu sebelah kiri (Extension).
  3.  Cari dan instal ekstensi bernama "**WSL**" (buatan Microsoft).
  4.  Setelah terinstal, kembali ke terminal Ubuntu, buat folder baru untuk belajar, lalu buka VS Code dari sana dengan mengetik:
    ```Terminal
    mkdir belajar_python
    cd belajar_python
    code .
    ```
    Perintah `code .` akan membuka VS Code yang secara otomatis terhubung langsung ke sistem Linux/WSL.

**Penjelasan Konsep Utama: Virtual Environment (Lingkungan Virtual)**
Sebelum kita mulai menulis kode, ada satu praktik standar industri yang wajib ktia ketahui sejak hari pertama: **Virtual Environment**.
  * **Apa itu?** Ruang kerja terisolasi untuk proyek Python.
  * **Mengapa butuh ini?** Bayangkan kita punya dua proyek. Proyek A butuh *library* (alat tambahan) versi 1.0, sedangkan Proyek B butuh versi 2.0. Jika kita menginstal alat tersebut langsung di komputer secara global, kedua proyek ini akan "bertengkar" dan salah satunya akan rusak.
  * **Visualisasi & Analogi**: Anggap komputer kita adalah sebuah bengkel besar. Jika kita mengerjakan mobil balap dan traktor di meja yang sama, baut dan olinya akan tercampur. *Virtual Environment* adalah membuat meja khusus untuk mobil balap, dan meja kerja lain khusus untuk traktor. Alat-alatnya tidak akan pernah tertukar.

**Kesalahan Umum Pemula**
  * **Kesalahan**: Menggunakan perintah `python` alih-alih `python3` di Ubuntu. Di beberapa sistem Linux, `python` merujuk pada Python versi 2 yang sudah sangat usang (mati sejak 2020).
  * **Solusi**: Selalu gunakan `python3` untuk menjalankan kode di terminal Ubuntu.

Mari kita pastikan "mesin" kita sudah menyala dengan baik. Coba buka terminal Ubuntu dan jalankan perintah `python3 --version`. Apa hasil atau angka versi yang muncul di layar?

```Terminal
bengs@Benkz:~$ python3 --version
Python 3.12.3
```

Python 3.12.3 adalah versi yang sangat modern dan cepat. Kita sudah memiliki mesin yang sangat mumpuni untuk belajar.

Sekarang mari kita buat "meja kerja khusus" kita yaitu **Virtual Environment**, agar proyek belajar kita tetap rapi dan terisolasi.

### Bagian 4

**Praktik: Membuat dan Mengaktifkan Virtual Environment**

Pastikan kita sedang berada di dalam folder `belajar-python` yang kita buat sebelumnya di terminal Ubuntu. Jika kita baru membuka terminal, ketik `cd belajar-python` lalu tekan Enter.

**Langkah 1: Membuat Virtual Environment**
Ketik perintah berikut di Terminal dan tekan Enter.

```Terminal
python3 -m venv .venv
```

*Penjelasan*:
  * `python3` memanggil mesin Python
  * `-m venv` memberitahu Python untuk menjalankan modul (alat bawaan) pembuatan *Virtual Environment*.
  * `.venv` dibagian akhir adalah nama folder untuk meja kerja kita. Kita bisa menamainya apa saja, tapi `.venv` atau `env` adalh standar industri.

Proses ini mungkin memakan waktu beberapa detik dan tidak akan memunculkan teks apa-apa jika berhasil.

**Langkah 2: Mengaktifkan Virtual Environment**

Meja kerjanya sudah ada, tapi kita belum duduk di sana. Untuk mengaktifkannya, ketik perintah ini:

```Terminal
source .venv/bin/activate
```

*Penjelasan*: Perintah `source` digunakan di Linux untuk membaca dan menjalankan perintah dari sebuah file. File `activate` ini berisi instruksi untuk mengubah jalur komputer kita agar fokus menggunakan Python yang ada di dalam folder `.venv` tersebut.

Coba jalankan kedua perintah di atas. Setelah kita menjalankan perintah `source .venv/bin/activate`, coba perhatikan tulisan di sebelah kiri tempat kita biasa mengetik perintah di Terminal.

Apakah ada perubahan atau tambahan kata barau yang muncul di paling kiri baris terminal?

**Jawaban:**

```terminal
bengs@Benkz:~/belajar-python$ source .venv/bin/activate
(.venv) bengs@Benkz:~/belajar-python$
```

Munculnya idikator `(.venv)` di paling kiri adalah konfirmasi bahwa *virtual environment* kita sudah aktif. Kita sekarang benar-benar berada di dalam "meja kerja khusus" yang terisolasi dan aman.

Mari kita lanjut ke tahap yang paling menarik: menulis instruksi pertama.

### Bagian 5

**Penjelasan Konsep Utama: Mode Skrip & Sintaksis Dasar**
Ada dua cara untuk memberikan instruksi kepada Python:
  1.  **Mode Interaktif**: Mengetik perintah satu per satu langsung di terminal. Ini cocok untuk menguji hitungan singkat.
  2.  **Mode Skrip**: Menulis daftar instruksi yang panjang di dalam sebuah dokumen teks (disebut *script* atau *file* Python), lalu menyuruh komputer membacanya dari atas ke bawah. Ini adalah standar yang digunakan untuk aplikasi nyata. File Python selalu diakhiri dengan ekstensi `.py`.

Untuk skrip pertama ini, kita akan menggunakan dua konsep dasar:
  * **Fungsi** `print()`: Ini adalah perintah bawaan untuk menyuruh Python mencetak teks atau data ke layar terminal. Jika Python adalah asistenmu, `print()` adalah cara asistenmu berbicara kepadamu. Teks yang ingin dicetak harus diapit oleh tanda kutip (bisa kutip satu `' '` atau kutip dua `" "`).
  * **Komentar** (`#`): Simbol pagar digunakan untuk menulis catatan. Segala teks yang berada di sebelah kanan simbol `#` tidak akan dibaca oleh mesin Python. Ini sangat penting agar programmer manusia biasa saling memahami maksud dari sebuah kode.

**Praktik: Menulis Skrip Pertama:**
Buka kembali aplikasi VS Code. Di panel sebelah kiri, pastikan kita berada di dalam folder `belajar-python`.
  1.  Buat sebuah file baru dan beri nama `main.py`
  2.  Ketik kode berikut tepat seperti yang tertulis:
      ```python
      # Program pertama
      print("Halo, dunia!")
      print("Saya siap membuat asisten otomatis.")
      ```
  3.  Simpan file tersebut (tekan `Ctrl + S` di windows).
  4.  Buka terminal Ubuntu (pastikan tulisan `(.venv)` masih ada di awal baris), lalu jalankan perintah ini untuk mengeksekusi skrip tersebut:
   
  ```terminal
  python3 main.py
  ```

Silakan coba ikuti langkah-langkah di atas. Apa kalimat yang muncul di layar terminal setelah kita menekan Enter?

**Jawaban:**

```python
# Program pertama
print("Halo, dunia!")
print("Saya siap membuat asisten otomatis.")
```

```terminal
(.venv) bengs@Benkz:~/belajar-python$ python3 main.py
Halo, dunia!
Saya siap membuat asisten otomatis.
(.venv) bengs@Benkz:~/belajar-python$
```

### Bagian 6

**Penjelasan Konsep Utama**: `input()` **(Membuat Asisten Mendengar)**
Sejauh ini, asisten kita baru bisa memberikan informasi atau "berbicara" menggunakan `print()`. Namun, aplikasi di dunia nyata (seperti mesin pencari Google atau layar *login* Netflix) pasti membutuhkan data dari penggunanya. Di sinilah kita menggunakan perintah `input()`.

**Visualisasi & Analogi**:
Jika `print()` adalah mulut asistenmu, maka `input()` adalah telinganya. Ketika Python membaca perintah `input()`, program akan **berhenti sejenak** (menunggu) sampai kita mengetikkan sesuatu di keyboard dan menekan tombol Enter.

Mari kita buat asisten kita lebih interaktif. Hapus kode lama di dalam file `main.py` kamu, lalu ganti dengan kode berikut:

```python
# Meminta asisten berkenalan
nama_pengguna = input("Halo! Siapa namamu? ")
print("Salam kenal,")
print(nama_pengguna)
```

**Penjelasan Singkat:**
Teks `"Halo! Siapa namamu? "` akan dicetak  ke layar untuk memberi tahu pengguna apa yang harus diketik. Lalu, kita menggunakan kata `nama_pengguna` sebagai **variabel**. Bayangkan variabel ini seperti sebuah kotak penyimpanan. Apa pun yang kita ketik di terminal akan dimasukkan ke dalam kotak itu. Di baris terakhir, kita menyuruh `print()` untuk membuka kotak tersebut dan menampilkan isinya ke layar.

**Latihan Praktik:**
Simpan kode tersebut, lalu jalankan lagi menggunakan perintah `python3 main.py` di layar terminal.

Setelah kita berhasil memasukkan nama, **bisakah kita mencoba memodifikasi kode tersebut (menambahkan perintah baru di bagian bawah) agar asisten kita juga menanyakan "Apa makanan favoritmu?" lalu asisten mencetak jawaban makanan favorit tersebut?**

**Jawaban:**

```python
# Meminta asisten berkenalan
nama_pengguna = input("Halo! Siapa namamu? ")
makanan_favorit = input("Apa makanan favoritmu? ")
print("Salam kenal,")
print(nama_pengguna)
print("Makanan favoritmu adalah,")
print(makanan_favorit)
```

```terminal
(.venv) bengs@Benkz:~/belajar-python$ python3 main.py
Halo! Siapa namamu? Bengs
Apa makanan favoritmu? Ketoprak
Salam kenal,
Bengs
Makanan favoritmu adalah,
Ketoprak
(.venv) bengs@Benkz:~/belajar-python$
```

Jika diperhatikan hasil di terminal, kata "Salam kenal," dan nama "Bengs" dicetak pada baris yang atas-bawah (terpisah), bukan? Begitu juga dengan bagian makanan favorit. Ini terjadi karena setiap kali asisten kita menjalankan perintah `print()`, ia akan secara otomatis menekan "Enter" (membuat baris baru) setelah selesai bicara.

Sebagai tantangan mini terkahir sebelum merampungkan **BAB 1**, mari kita buat hasil cetakannya lebih natural, yaitu menyambung dalam satu baris.

Di Python, kita bias menggabungkan teks langsung dengan isi dari sebuah variabel di dalam satu perintah `print()` yang sama. Caranya adalah dengan memisahkan menggunakan tanda koma `,`.

Contoh seperti ini:

```Python
warna_baju = input("Apa warna bajumu? ")
# Menggabungkan teks dan variabel dengan koma
print("Wah, warna bajumu adalah", warna_baju)
```

(*Catatan: Python akan otomatis menyisipkan satu spasi di posisi tanda koma tersebut saat dicetak ke layar*).

Berdasarkan contoh di atas, bisakah kamu memodifikasi kodemu agar asistenmu mencetak persis seperti ini:
`Salam kenal, Bengs` (di baris pertama)
`Makanan favoritmu adalah Ketoprak` (di baris kedua)

**Jawaban:**

```python
# Meminta asisten berkenalan
nama_pengguna = input("Halo! Siapa namamu? ")
makanan_favorit = input("Apa makanan favoritmu? ")
print("Salam kenal,", nama_pengguna)
print("Makanan favoritmu adalah", makanan_favorit)
```

```terminal
(.venv) bengs@Benkz:~/belajar-python$ python3 main.py
Halo! Siapa namamu? Bengs
Apa makanan favoritmu? Ketoprak
Salam kenal, Bengs
Makanan favoritmu adalah Ketoprak
(.venv) bengs@Benkz:~/belajar-python$
```

### Bagian 7

**Kesalahan Umum & Best Practices (Praktik Terbaik)**
Sebagai programmer, melihat *error* atau pesan kesalahan bertebaran di terminal adalah hal yang sangat normal (bahkan programmer senior pun mengalaminya setiap hari). Berikut adalah dua kesalahan umum bagi pemula di tahap ini:
  1.  **Name Error (Salah Ketik Nama Variabel)**
      * **Kesalahan**: Kita membuat variabel `nama_pengguna = "Bengs"`, tetapi saat di-*print*, kita mengetik `print(Nama_Pengguna)`.
      * **Mengapa Error?** Python itu *case-sensitive* (membedakan huruf besar dan kecil). `nama` dan `Nama` dianggap sebagai dua kota yang berbeda.
      * **Solusi**: Selalu pastikan ejaan dan huruf besar/kecil sama persis.
  2.  **Syntax Error (Lupa Tanda Kutip atau Kurung)**
      * **Kesalahan**: `print("Halo, Bengs)` -> Lupa tanda kutip penutup.
      * **Solusi**: VS Code biasanya akan memberi warna merah atau garis bawah jika kita melupakan tanda baca. Selalu perhatikan warna kode.

### Bagian 8

**Mini Project: Generator Cerita Pendek (Mad Libs)**
Untuk mengunci pemahamanmu di BAB 1, mari kita buatkan satu proyek kecil. Spesifikasinya seperti ini:
  1.  Buat asisten kita menanyakan 3 hal kepada pengguna (gunaka `input()`):
      * Nama pahlawan (contoh variabel: `nama`)
      * Nama tempat (contoh: variabel: `tempat`)
      * Kekuatan super (contoh variabel: `kekuatan`)
  2.  Setelah pengguna menjawab ketiga pertanyaan tersebut, asisten kita harus mencetak sebuah cerita singkat yang menggabungkan ketiga jawaban tadi dalam satu paragraf bersambung.

**Jawaban:**

```python
nama_pahlawan = input("Siapa nama pahlawan? ")
nama_markas = input("Di mana markasmu? ")
kekuatan = input("Apa kekuatan supermu? ")

print("===== CERITA HARI INI =====")
print("Beliau adalah seorang pahlawan bernama", nama_pahlawan)
print("Lokasi markas beliau di", nama_markas)
print("Kekutatan super beliau adalah", kekuatan)
```

```terminal
(.venv) bengs@Benkz:~/belajar-python$ python3 mini-projects/mini_project_1.py 
Siapa nama pahlawan? Bengs
Di mana markasmu? Ciputat
Apa kekuatan supermu? Ngoding
===== CERITA HARI INI =====
Beliau adalah seorang pahlawan bernama Bengs
Lokasi markas beliau di Ciputat
Kekutatan super beliau adalah Ngoding
(.venv) bengs@Benkz:~/belajar-python$ 
```

**Kesimpulan BAB 1**
Di bab pertama ini, kita sudah menguasai fondasi yang sangat penting:
  * Paham bahwa Python adalah bahasa penerjemah instruksi ke mesin.
  * Bisa membuat dan masuk ek "meja kerja khusus" (*Virtual Environment*)
  * Bisa menyuruh komputer berbicara (`print()`) dan mendengar (`input()`).
  * Bisa menyimpan informasi di dalam kotak penyimpanan (`variabel`).
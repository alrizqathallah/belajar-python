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

---

## BAB 2: Tipe Data & Variabel

### Bagian 1

**1. Tujuan Pembelajaran**
Di bab ini, kita akan mempelajari jenis-jenis informasi yang bisa diproses oleh Python (Tipe Data), cara mengubah tipe data satu ke tipe lainnya, dan aturan penamaan variabel yang sesuai standar industri.

**2. Penjelasan Konsep Utama: Apa itu Tipe Data?**
Di Bab 1, kita sepakat bahwa variabel adalah "kotak penyiimpanan". Namun, di dunia nyata, kita tidak bisa menyimpan semua hal di kotak yang sama. Jika kita ingin menyinmpan air, kita menggunakan botol, bukan kardus.

Sama halnya dengan Python. Python perlu tahu *jenis* data apa yang sedang ia tangani agar tidak salah memprosesnya. Ada 4 tipe data dasar (fondasi) di Python yang wajib kita ketahui:
  * **String** (`str`): Digunakan untuk menyimpan **teks**. Ciri utamanya adalah selalu diapit oleh tanda kutip ganda `" "` atau tunggal `' '`.
    * Contoh: `"Ciputat"`, `"Bengs"`, atau bahkan angka yang dikelilingi kutip seperti `"100"`.
  * **Integer** (`int`): Digunakan untk menyimpan **bilangan bulat** (angka yang tidak memiliki koma/desimal). Bisa positif atau negatif.
    * *Contoh*: `25`, `1000`, `-5`.
  * **Float** (`float`): Digunakan untuk menyimpan **bilangan desimal**. Penting diingat: standar internasional dan Python menggunakan **titik** (`.`) untuk desimal, bukan koma (`,`).
    * *Contoh*: `3.14`, `65.5`, `-0.01`.
  * **Boolean** (`bool`): Ini adalah tipe data spesial yang hanya bisa berisi dua kemungkinan: `True` (Benar) atau `False` (Salah). Tipe ini sangat berguna nanti saat kita ingin membuat asisten kita bisa mengambil keputusan. (Catatan: Huruf pertama wajib kapital).

Sebelum kita mencoba menuliskannya ke dalam kode, mari kita uji pemahaman konsep ini.

Jika asisten kita ingin menyimpan data tentang suhu tubuh seseorang, misalnya **36.7 derajat Celcius**, tipe data apa dari keempat pilihan di atas yang paling tepat untuk menyimpan angka tersebut?

**Jawaban:**

> Menggunakan tipe data Float `float`.

### Bagian 2

**Penjelasan Konsep Utama: Memeriksa Tipe Data & F-String**
  1.  **Mengecek Tipe Data dengan `type()`
      Terkadang, kita menerima kotak data dan tidak tahu apa isinya. Python memiliki fungsi bawaan bernama `type()` untuk mengintip jenis data di dalam kotak tersebut.
  2.  **Teks Modern dengan F-String (Format String)**
      Di Bab 1, kita menggabungkan teks dan variabel menggunakan koma `,`. Mulai sekarang, kita akan menggunakan cara standar industri modern yang disebut **f-string**.
      Caranya sangat mudah: tambahkan huruf `f` tepat sebelum tanda kutip pembuka, lalu masukkan varibel ke dalam kurung kurawal `{}`. Ini membuat kode jauh lebih rapih dan mudah dibaca.

**Contoh Kode**:
Buka file `main.py`, hapus isinya, dan coba kode berikut:

```python
nama = "Bengs"      # String (str)
umur = 25           # Integer (int)
suhu = 36.7         # Float (float)
sedang_belajar = True  # Boolean (bool)

# Menggunakan f-string (perhatikan huruf 'f' di depan tanda kutip)
print(f"Halo, nama saya {nama} dan saya berumur {umur} tahun.")

# Mengecek tipe data
print(type(suhu))
```

**Penjelasan Konsep Utama: Konversi Tipe Data (Type Casting)**
Ini adalah aturan emas di Python: **Fungsi** `input()` **akan SELALU menghasilkan data berupa String (Teks)**.

**Visualisasi & Analogi**:
Bayangkan kita memiliki angka balok mainan kayu yang bertuliskan angak `5`. Walaupaun merpresentasikan angka lima, bahannya tetaplah "kayu" (String). Kita tidak bisa menggunakan balok kayu itu untuk operasi matematika sungguhan sebelum kita mengubahnya menjadi "angka asli" (Integer).

JIka kita mengambil umur dari pengguna:
`umur_pengguna = input("Berapa umurmu? ")`
Jika pengguna mengetik `25`, komputer menyimpannya sebagai teks `"25"`, bukan angka `25`.
Jika kita mencoba menghitung `"25" + 5`, komputer akan *error* karena ia tidak tahu cara menambahkan teks dengan angka.

Untuk mengubah bentuk data, kita menggunakan alat pengubah (konversi):
  * `int()`: Mengubah teks/float menjadi integer. Contoh: `int("25")` menajdi `25`.
  * `float()`: Mengubah teks/integer menjadi desimal. Contoh: `float("10")` menjadi `10.0`.
  * `str()`: Mengubah angka menjadi teks. Contoh: `str(100)` menjadi `"100"`.

**Latihan Praktik & Tantangan Logika**:
Mari kita uji konsep ini. Kita ingin membuat program **kalkulator tahun lahir**.
  1.  Minta pengguna memasukkan tahun lahir mereka menggunakan `input()`.
  2.  Hitung umur mereka saat ini (kita bisa gunakan rumus: `2026 - tahun_lahir`).
  3.  Cetak hasilnya menggunakan **f-string**.

*Petunjuk Penting*: Ingat, hasil dari `input()` adalah String. Kita harus mengubahnya menjadi Integer terlebih dahulu sebelum bisa dikurangi dari 2026.

**Jawaban:**

```python
nama_pengguna = input("Siapa nama Anda? ")
tahun_lahir = input("Kapan tahun lahir Anda? ")
umur_pengguna = 2026 - int(tahun_lahir)

print(f"Halo {nama_pengguna}, umur anda adalah {umur_pengguna} tahun")
```

```terminal
(.venv) bengs@Benkz:~/belajar-python$ python3 main.py 
Siapa nama Anda? Bengs
Kapan tahun lahir Anda? 1998
Halo Bengs, umur anda adalah 28 tahun
(.venv) bengs@Benkz:~/belajar-python$
```

### Bagian 3

**Penjelasan Konsep Utama: Aturan Penamaan Variabel**
Saat membuat variabel `nama_pengguna` dan `tahun_lahir`, kita secara tidak sadar sudah menggunakan standar industri yang disebut **Snake_Case**.

Di Python, aturan emas penamaan variabel adalah:
  1.  **Gunakan huruf kecil semua** dan pisahkan kata dengan **garis bawah** (`_`). Contoh: `total_harga`, bukan `TotalHarga` atau `totalHarga`.
  2.  **Tidak boleh diawali angaka.** `1_nama` itu salah, `nama_1` itu benar.
  3.  **Harus deskriptif**. Jangan gunakan singkatan yang membingungkan seperti `x = 28` atau `n = "Bengs"`. Gunakan `umur = 28` dan `nama = "Bengs"`.

**Penjelasan Konsep Utama: Membersihkan Teks (String Methods)**
Di dunia nyata, kita tidak bisa mengontrol bagaimana pengguna mengetik. Terkadang pengguna tidak sengaja menekan tombol spasi atau salah menggunakan hufuh kapital (misalnya mengetik `bENGS` atau `bengs`).

Python memiliki "alat pembersih otomatis" untuk tipe data String yang disebut **String Methods**. Ini seperti sikat dan sabun untuk membersihkan dat teks kita.
  * `.upper()`: Mengubah semua huruf menjadi KAPITAL.
  * `.lower()`: Mengubah semua huruf menjadi kecil.
  * `.title()`: Mengubah Huruf Pertama Setiap Kata Menjadi Kapital.
  * `.strip()`: Menghapus spasi ekstra di awal dan di akhir teks.

**Contoh Penggunaan:**

```python
teks_berantakan = "     bENgs "
teks_bersih = teks_berantakan.strip().title()     # Menghapus spasi DULU, lalu membuat awalan kapital

print(f"Hasil sebelum dibersihkan: '{teks_berantakan}'")
print(f"Hasil sebelum dibersihkan: '{teks_bersih}'")
```

**Mini Project BAB 2: Profiler Pengguna**

Untuk menutup BAB 2, mari kita gabungkan smeua yang sudah kita pelajari (Tipe Data, Konversi Tipe Data, F-String, dan String Methods) ke dalam satu program.

**Misi Kamu:**
Buat program yang meminta 3 data dari pengguna:
  1.  **Nama Lengkap** (Pastikan saat dicetak, awal kata selalu huruf kapital menggunakan string method, walaupun pengguna mengitiknya dengan huruf kecil semua).
  2.  **Tahun Lahir** (Gunakan untuk menghitung umur di tahun 2026).
  3.  **Tinggi Badan dalam cm** (Ubah input ini menjadi tipe data desimal / `float`, lalu bagi dengan 100 agar berubah menjadi satuan meter. Contoh: 170 menjadi 1.7).

Cetak hasilnya dalam satu kalimat menggunakan F-String, misalnya: "Halo Bengs, umurmu 28 tahun dan tinggi badanmu 1.7 meter."

**Jawaban:**

```Python
nama_lengkap = input("Halo, siapa namamu? ")
tahun_lahir = input("Tahun berapa kamu lahir? ")
tinggi_cm = input("Berapa tinggi badan mu? ")

nama_diperbaiki = nama_lengkap.strip().title()
umur_pasti = 2026 - int(tahun_lahir)
tinggi_m = float(tinggi_cm) / 100

print(f"Halo {nama_diperbaiki}, umurmu {umur_pasti} tahun dan tinggi badanmu {tinggi_m} meter")
```

```terminal
(.venv) bengs@Benkz:~/belajar-python$ python3 mini-projects/mini_project_2.py
Halo, siapa namamu? bENgs
Tahun berapa kamu lahir? 1998
Berapa tinggi badan mu? 170
Halo Bengs, umurmu 28 tahun dan tinggi badanmu 1.7 meter
```
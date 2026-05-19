# Python

## BAB 1: Pengenalan & Persiapan

### Bagian 1

**1. Tujuan Pembelajaran**
Fokus kita di tahap pertama ini adalah memahami esensi bahasa Python dan mengapa industri sangat menyukainya, sebelum kita menyiapkan perangkatnya.

**2. Penjelasan Konsep Utama: Apa itu Python?**
Python adalah bahasa pemrograman tingkat tinggi. Istilah "tingkat tinggi" berarti sintaksisnya (aturan penulisannya) dirancang agar sangat mudah dibaca oleh manusia, karena bentuknya mendekati bahasa inggris dasar.

**Visualisasi & Analogi**
Bayangkan kita sedang memberikan resep kepada seorang asisten koki (komputer) untuk membuat kue.

- Jika menggunakan bahasa pemrograman tingkat rendah, kita harus menjelaskan instruksi mekanis yang sangat rumit: "Posisikan sendok pada koordinat x, y, lalu gerakkan melingkar dengan kecepatan 2 m/s."
- Dengan bahasa tingkat tinggi seperti Python, kita cukup memberi instruksi sederahan: `aduk_adonan()`. Python memiliki "penerjemah" di belakang layar yang akan mengubah teks sederhana itu menjadi kode biner rumit yang dimengerti mesin.

**Study Kasus: Mengapa Python?**
Di dunia industri modern, efisiensi waktu adalah segalanya. Python digunakan oleh raksasa teknologi (seperti Google, Netflix dan Instagram) karena developer bisa menulis lebih sedikit baris kode untuk mencapai tujuan yang sama dibandingkan bahasa lain. Penggunaannya sangat luas: dari membangun sistem web (Backend), menganalisis jutaan baris data keuangan (Data Science), hingga melatih kecerdasan buatan (Machine Learning).

Sebelum kita melangkah ke proses instalasi Python dan Editor kodenya (seperti VS Code), mari kita bangun pola pikir pemecah masalah. Jika kita memiliki asisten pintas yang bisa diprogram untuk melakukan tugas berulang di komputer, apa yang pertama kali ingin kita otomatisasikan atau berikan kepadanya?

Untuk memberi sedikit gambaran, ini beberapa tugas yang sering diserahkan orang kepada Python agar mereka tidak perlu bekerja manual:

- **Merapikan File**: Otomatis memilih ratusan file di folder "Downloads" yang berantakan (otomatis memindahkan gambar ke folder Gambar, dokumen ke folder Dokumen, dst).
- **Mengambil Data**: Mengunduh daftar harga barang dari toko _online_ setiap jam untuk mencari tahu kapan ada diskon termurah.
- **Pesan Otomatis**: Mengirim pesan WhatsApp atau email ke 50 teman dengan menyebutkan nama mereka masing-masing tanpa harus _copy-paste_ satu per satu.

Hal-hal seperti itulah yang akan perlahan kita pelajari cara membuatnya. Namun, sebelum asisten kita bisa bekerja, kita harus meyiapkan "alat kerjanya" terlebih dahulu di komputer kita.

### Bagian 2

**Penjelasan Konsep: Alat Kerja Python**
Untuk menulis dan menjalankan Python, kita secara umum membutuhkan dua hal:

1.  **Python Interpreter (Penerjemahan)**: Ini adalah mesin utamanya. Komputer tidak mengerti bahasa Python, ia hanya mengerti angka 1 dan 0. Interpreter ini bertugas membaca tulisan Python kita, lalu menerjemahkannya menjadi 1 dan 0 secara _rela-time_ agar komputer bisa menjalankannya.
2.  **Code Editor (Penyunting Kode)**: Ini adalah "buku tulis" tempat kita merangkai kode. Kita sebenarnya bisa menulis kode Python di _Notepad_, tetapi itu akan sangat sulit. Kita akan menggunakan **Visual Studio Code (VS Code)**, editor gratis yang sangat populer di industri karena bisa memberi warna pada kode dan memberi tahu jika ada salah ketik (typo).

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

- **Apa itu?** Ruang kerja terisolasi untuk proyek Python.
- **Mengapa butuh ini?** Bayangkan kita punya dua proyek. Proyek A butuh _library_ (alat tambahan) versi 1.0, sedangkan Proyek B butuh versi 2.0. Jika kita menginstal alat tersebut langsung di komputer secara global, kedua proyek ini akan "bertengkar" dan salah satunya akan rusak.
- **Visualisasi & Analogi**: Anggap komputer kita adalah sebuah bengkel besar. Jika kita mengerjakan mobil balap dan traktor di meja yang sama, baut dan olinya akan tercampur. _Virtual Environment_ adalah membuat meja khusus untuk mobil balap, dan meja kerja lain khusus untuk traktor. Alat-alatnya tidak akan pernah tertukar.

**Kesalahan Umum Pemula**

- **Kesalahan**: Menggunakan perintah `python` alih-alih `python3` di Ubuntu. Di beberapa sistem Linux, `python` merujuk pada Python versi 2 yang sudah sangat usang (mati sejak 2020).
- **Solusi**: Selalu gunakan `python3` untuk menjalankan kode di terminal Ubuntu.

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

_Penjelasan_:

- `python3` memanggil mesin Python
- `-m venv` memberitahu Python untuk menjalankan modul (alat bawaan) pembuatan _Virtual Environment_.
- `.venv` dibagian akhir adalah nama folder untuk meja kerja kita. Kita bisa menamainya apa saja, tapi `.venv` atau `env` adalh standar industri.

Proses ini mungkin memakan waktu beberapa detik dan tidak akan memunculkan teks apa-apa jika berhasil.

**Langkah 2: Mengaktifkan Virtual Environment**

Meja kerjanya sudah ada, tapi kita belum duduk di sana. Untuk mengaktifkannya, ketik perintah ini:

```Terminal
source .venv/bin/activate
```

_Penjelasan_: Perintah `source` digunakan di Linux untuk membaca dan menjalankan perintah dari sebuah file. File `activate` ini berisi instruksi untuk mengubah jalur komputer kita agar fokus menggunakan Python yang ada di dalam folder `.venv` tersebut.

Coba jalankan kedua perintah di atas. Setelah kita menjalankan perintah `source .venv/bin/activate`, coba perhatikan tulisan di sebelah kiri tempat kita biasa mengetik perintah di Terminal.

Apakah ada perubahan atau tambahan kata barau yang muncul di paling kiri baris terminal?

**Jawaban:**

```terminal
bengs@Benkz:~/belajar-python$ source .venv/bin/activate
(.venv) bengs@Benkz:~/belajar-python$
```

Munculnya idikator `(.venv)` di paling kiri adalah konfirmasi bahwa _virtual environment_ kita sudah aktif. Kita sekarang benar-benar berada di dalam "meja kerja khusus" yang terisolasi dan aman.

Mari kita lanjut ke tahap yang paling menarik: menulis instruksi pertama.

### Bagian 5

**Penjelasan Konsep Utama: Mode Skrip & Sintaksis Dasar**
Ada dua cara untuk memberikan instruksi kepada Python:

1.  **Mode Interaktif**: Mengetik perintah satu per satu langsung di terminal. Ini cocok untuk menguji hitungan singkat.
2.  **Mode Skrip**: Menulis daftar instruksi yang panjang di dalam sebuah dokumen teks (disebut _script_ atau _file_ Python), lalu menyuruh komputer membacanya dari atas ke bawah. Ini adalah standar yang digunakan untuk aplikasi nyata. File Python selalu diakhiri dengan ekstensi `.py`.

Untuk skrip pertama ini, kita akan menggunakan dua konsep dasar:

- **Fungsi** `print()`: Ini adalah perintah bawaan untuk menyuruh Python mencetak teks atau data ke layar terminal. Jika Python adalah asistenmu, `print()` adalah cara asistenmu berbicara kepadamu. Teks yang ingin dicetak harus diapit oleh tanda kutip (bisa kutip satu `' '` atau kutip dua `" "`).
- **Komentar** (`#`): Simbol pagar digunakan untuk menulis catatan. Segala teks yang berada di sebelah kanan simbol `#` tidak akan dibaca oleh mesin Python. Ini sangat penting agar programmer manusia biasa saling memahami maksud dari sebuah kode.

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
Sejauh ini, asisten kita baru bisa memberikan informasi atau "berbicara" menggunakan `print()`. Namun, aplikasi di dunia nyata (seperti mesin pencari Google atau layar _login_ Netflix) pasti membutuhkan data dari penggunanya. Di sinilah kita menggunakan perintah `input()`.

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
Teks `"Halo! Siapa namamu? "` akan dicetak ke layar untuk memberi tahu pengguna apa yang harus diketik. Lalu, kita menggunakan kata `nama_pengguna` sebagai **variabel**. Bayangkan variabel ini seperti sebuah kotak penyimpanan. Apa pun yang kita ketik di terminal akan dimasukkan ke dalam kotak itu. Di baris terakhir, kita menyuruh `print()` untuk membuka kotak tersebut dan menampilkan isinya ke layar.

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

(_Catatan: Python akan otomatis menyisipkan satu spasi di posisi tanda koma tersebut saat dicetak ke layar_).

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
Sebagai programmer, melihat _error_ atau pesan kesalahan bertebaran di terminal adalah hal yang sangat normal (bahkan programmer senior pun mengalaminya setiap hari). Berikut adalah dua kesalahan umum bagi pemula di tahap ini:

1.  **Name Error (Salah Ketik Nama Variabel)**
    - **Kesalahan**: Kita membuat variabel `nama_pengguna = "Bengs"`, tetapi saat di-_print_, kita mengetik `print(Nama_Pengguna)`.
    - **Mengapa Error?** Python itu _case-sensitive_ (membedakan huruf besar dan kecil). `nama` dan `Nama` dianggap sebagai dua kota yang berbeda.
    - **Solusi**: Selalu pastikan ejaan dan huruf besar/kecil sama persis.
2.  **Syntax Error (Lupa Tanda Kutip atau Kurung)**
    - **Kesalahan**: `print("Halo, Bengs)` -> Lupa tanda kutip penutup.
    - **Solusi**: VS Code biasanya akan memberi warna merah atau garis bawah jika kita melupakan tanda baca. Selalu perhatikan warna kode.

### Bagian 8

**Mini Project: Generator Cerita Pendek (Mad Libs)**
Untuk mengunci pemahamanmu di BAB 1, mari kita buatkan satu proyek kecil. Spesifikasinya seperti ini:

1.  Buat asisten kita menanyakan 3 hal kepada pengguna (gunaka `input()`):
    - Nama pahlawan (contoh variabel: `nama`)
    - Nama tempat (contoh: variabel: `tempat`)
    - Kekuatan super (contoh variabel: `kekuatan`)
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

- Paham bahwa Python adalah bahasa penerjemah instruksi ke mesin.
- Bisa membuat dan masuk ek "meja kerja khusus" (_Virtual Environment_)
- Bisa menyuruh komputer berbicara (`print()`) dan mendengar (`input()`).
- Bisa menyimpan informasi di dalam kotak penyimpanan (`variabel`).

---

## BAB 2: Tipe Data & Variabel

### Bagian 1

**1. Tujuan Pembelajaran**
Di bab ini, kita akan mempelajari jenis-jenis informasi yang bisa diproses oleh Python (Tipe Data), cara mengubah tipe data satu ke tipe lainnya, dan aturan penamaan variabel yang sesuai standar industri.

**2. Penjelasan Konsep Utama: Apa itu Tipe Data?**

Di Bab 1, kita sepakat bahwa variabel adalah "kotak penyiimpanan". Namun, di dunia nyata, kita tidak bisa menyimpan semua hal di kotak yang sama. Jika kita ingin menyinmpan air, kita menggunakan botol, bukan kardus.

Sama halnya dengan Python. Python perlu tahu _jenis_ data apa yang sedang ia tangani agar tidak salah memprosesnya. Ada 4 tipe data dasar (fondasi) di Python yang wajib kita ketahui:

- **String** (`str`): Digunakan untuk menyimpan **teks**. Ciri utamanya adalah selalu diapit oleh tanda kutip ganda `" "` atau tunggal `' '`.
  - Contoh: `"Ciputat"`, `"Bengs"`, atau bahkan angka yang dikelilingi kutip seperti `"100"`.
- **Integer** (`int`): Digunakan untk menyimpan **bilangan bulat** (angka yang tidak memiliki koma/desimal). Bisa positif atau negatif.
  - _Contoh_: `25`, `1000`, `-5`.
- **Float** (`float`): Digunakan untuk menyimpan **bilangan desimal**. Penting diingat: standar internasional dan Python menggunakan **titik** (`.`) untuk desimal, bukan koma (`,`).
  - _Contoh_: `3.14`, `65.5`, `-0.01`.
- **Boolean** (`bool`): Ini adalah tipe data spesial yang hanya bisa berisi dua kemungkinan: `True` (Benar) atau `False` (Salah). Tipe ini sangat berguna nanti saat kita ingin membuat asisten kita bisa mengambil keputusan. (Catatan: Huruf pertama wajib kapital).

Sebelum kita mencoba menuliskannya ke dalam kode, mari kita uji pemahaman konsep ini.

Jika asisten kita ingin menyimpan data tentang suhu tubuh seseorang, misalnya **36.7 derajat Celcius**, tipe data apa dari keempat pilihan di atas yang paling tepat untuk menyimpan angka tersebut?

**Jawaban:**

> Menggunakan tipe data Float `float`.

### Bagian 2

**Penjelasan Konsep Utama: Memeriksa Tipe Data & F-String**

1.  \*\*Mengecek Tipe Data dengan `type()`
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
Jika kita mencoba menghitung `"25" + 5`, komputer akan _error_ karena ia tidak tahu cara menambahkan teks dengan angka.

Untuk mengubah bentuk data, kita menggunakan alat pengubah (konversi):

- `int()`: Mengubah teks/float menjadi integer. Contoh: `int("25")` menajdi `25`.
- `float()`: Mengubah teks/integer menjadi desimal. Contoh: `float("10")` menjadi `10.0`.
- `str()`: Mengubah angka menjadi teks. Contoh: `str(100)` menjadi `"100"`.

**Latihan Praktik & Tantangan Logika**:

Mari kita uji konsep ini. Kita ingin membuat program **kalkulator tahun lahir**.

1.  Minta pengguna memasukkan tahun lahir mereka menggunakan `input()`.
2.  Hitung umur mereka saat ini (kita bisa gunakan rumus: `2026 - tahun_lahir`).
3.  Cetak hasilnya menggunakan **f-string**.

_Petunjuk Penting_: Ingat, hasil dari `input()` adalah String. Kita harus mengubahnya menjadi Integer terlebih dahulu sebelum bisa dikurangi dari 2026.

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

- `.upper()`: Mengubah semua huruf menjadi KAPITAL.
- `.lower()`: Mengubah semua huruf menjadi kecil.
- `.title()`: Mengubah Huruf Pertama Setiap Kata Menjadi Kapital.
- `.strip()`: Menghapus spasi ekstra di awal dan di akhir teks.

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

---

## BAB 3: Operator & Ekspresi

### Bagian 1

**1. Tujuan Pembelajaran**

Di bagian pertama bab ini, kita akan menguasai cara menjadikan Python sebagai kalkulator super canggih (Operator Aritmatika) dan bagaimana menyuruh Python membandingkan dua buah data untuk mencari kebenaran (Operator Perbandingan).

**2. Penjelasan Konsep Utama: Operator Aritmatika (Matematika)**

Sama seperti matematika dasar di sekolah, Python menggunakan simbol untuk menghitung. Namun, ada beberapa simbol khusus yang menjadi "senjata rahasia" para _programmer_.

- `+` (Tambah) dan `-` (kurang)
- `*` (Kali) -> _Perhatikan: kita menggunakan bintang/asterisk, bukan "x"_.
- `/` (Bagi) -> _Menghasilkan angka desimal (`float`). Contoh: `10/2` menjadi `5.0`._
  **Senjata Rahasia Python:**
- `//` (Pembagian Bulat / _Floor Division_) -> Membagi angka, tapi membuang desimalnya (dibulatkan ke bawah). Contoh `10 // 3` hasilnya `3`.
- `**` (Pangkat) -> Contoh: `2 ** 3` artinya 2 pangkat 3 (hasilnya 8).
- `%` (Modulus / Sisa Bagi) -> Ini yang **paling sering dipakai di industri**. Modulus mengitung _sisa_ dari sebuah pembagian.

**Visualisasi & Analogi Modulus (`%`)**

Bayangkan kita punya 10 butir peluru dan kita harus membaginya rata kepada 3 rekan tim.
Masing-masing rekan mendapatkan 3 butir. Nah, ada **sisa 1 peluru** ditangan, bukan?
Itulah Modulus! `10 % 3` hasilnya adalah `1`.
(_Bocoran: Modulus sangat sering digunakan untuk mengecek apakah sebuah angka ganjil atau genap. Angka genap jika di-modulus 2 hasilnya pasti 0_).

**3. Penjelasan Konsep Utama: Operator Perbandingan**

Python bisa bertindak sebagai juri. Kita bisa meminta Python membandingkan dua nilai, dan ia akan **selalu** menjawab dengan tipe data Boolean: `True` (Benar) atau `False` (Salah).

- `==` (Sama Dengan) -> Sangat penting! Sama dengan ganda digunakan untuk membandingkan. Sama dengan tunggal `=` hanya untuk memasukkan barang ke dalam kotak variabel.
- `!=` (Tidak Sama Dengan) -> Tanda seru artinya "Tidak".
- `>` (Lebih besar dari) dan `<` (lebih kecil dari)
- `>=` (Lebih besar atau sama dengan) dan `<=` (Lebih kecil atau sama dengan)

**Contoh Kode: Membandingkan Status**

```python
peluru_senjata = 0

# Python akan mengecek: Apakah peluru sama dengan 0?
butuh_reload = (peluru_senjata == 0)

print(f"Apakah harus reload senjata? {butuh_reload}")
```

_Hasilnya akan mencetak `True` karena peluru memang bernilai 0_.

**Kesalahan Umum Pemula**

- **Kesalahan**: Menggunakan `=` saat ingin membandingkan. `if harga = 10000:` (Ini akan menyebabkan _Error_ besar).
- **Solusi**: Ingat, `=` untuk **memberi** nilai (Assignment), `==` untuk **mengecek** nilai (comparasion).

**Latihan Praktik**

Mari kita uji konsep Aritmatika dan Perbandingan ini dalam satu kode.

Tulis program sederhana yang melakukan hal berikut:

- Buat variabel `jumlah_hari` dengan nilai `45`
- Hitung ada **berapa minggu penuh** dalam 45 hari menggunakan _Floor Division_ (`//`), simpan di variabel `minggu`. (_Petunjuk: 1 minggu = 7 hari_)
- Hitung **sisa harinya** menggunakan Modulus (`%`), simpan di variabel `sisa_hari`.
- Cek apakah `sisa_hari` tersebut persis sama dengan `3` menggunakan operator perbandingan (`==`), simpan hasilnya di variabel `cek_sisa`.
- Cetak semuanya menggunakan f-string.

**Jawaban:**

```python
jumlah_hari = 45
pekan = jumlah_hari // 7
sisa_hari = jumlah_hari % 7
cek_sisa = sisa_hari == 3

print(f"Jumlah hari      : {jumlah_hari}")
print(f"Minggu penuh     : {pekan}")
print(f"Sisa hari        : {sisa_hari}")
print(f"Apakah sisa = 3? : {cek_sisa}")
```

```terminal
(.venv) bengs@Benkz:~/belajar-python$ python3 main.py
Jumlah hari      : 45
Minggu penuh     : 6
Sisa hari        : 3
Apakah sisa = 3? : True
(.venv) bengs@Benkz:~/belajar-python$
```

### Bagian 2

**1. Penjelasan Konsep Utama: Operator Logika**

Dalam dunia nyata, keputasan sering kali tidak hanya bergantung pada satu syarat, melainkan gabungan dari beberapa syarat. Python menggunakan tiga operator logika utama: `and`, `or`, dan `not`.

- `and` (**Dan**): Akan menghasilkan `True` **HANYA JIKA** semua syarat benilai `True`.
  - _Anologi_: Syarat melamar kerja adalah "Punya Ijazah" `and` "Lulus Tes". Jika kamu punya ijazah tapi gagal tes, kamu tidak terima (`False`).
- `or` (**Atau**): Akan menghasilkan `True` **JIKA SALAH SATU SAJA** syarat bernilai `True`.
  - _Anologi_: Bayar belanjaan bisa pakai "Uang Tunai" `or` "Kartu Debit". Jika kamu bawa kartu tapi tidak bawa uang tunai, kamu tetap bisa bayar (`True`).
- `not` (**Bukan/Kebalikan**): Membalik fakta. Jika `True` menjadi `False`, dan sebaliknya.

**Contoh Kode:**

```python
punya_sim = True
umur = 20

# Syarat boleh mengemudi: Punya SIM DAN umur minimal 17 tahun
boleh_mengemudi = punya_sim and (umur >= 17)
print(f"Boleh mengemudi? {boleh_mengemudi}")    # Hasilnya: True
```

**2. Penjelasan Konsep Utama: Operator Assignment Gabungan (Augmented Assignment)**

Seorang _programmer_ sangat menyukai efisien (malas mengetik hal yang berulang). Jika kita memiliki variabel `skor = 10` dan ingin menambahkan 5 ke dalamnya, cara dasar yang kita gunakan adalah `skor = skor + 5`.

Namun, di industri, kita menggunakan jalan pintas:

- `+=` (Tambah dan masukkan) -> `skor += 5`
- `-=` (Kurang dan masukkan) -> `skor -= 5`
- `*=` (Kali dan masukkan) -> `skor *= 2`

**3. Penjelasan Konsep Utama: Operator Membership**

Digunakan untuk mengecek apakah sebuah elemen "berada di dalam" elemen yang lebih besar. Menggunakan `in` atau `not in`.

```python
teks = "Halo Bengs, selamat pagi!"
cek_nama = "Bengs" in teks
print(f"Apakah ada kata Bengs? {cek_nama}")   # Hasilnya: True
```

**Kesalahan Umum & Best Practices**

- **Kesalahan**: Menggabungkan logikan tanpa tanda kurung yang jelas. Misalnya `a > 5 and b < 10 or c == 0`. Ini bisa membuat Python (dan kita sendiri) bingung mana yang dikerjakan duluan.
- **Solusi**: Selalu gunakan tanda kurung `()` untuk mengelompokkan logika agar mudah dibaca, contoh: `(a > 5 and b < 10) or (c == 0)`.

**Mini Project BAB 3: Sistem Pengecekan Syarat Beasiswa**

Untuk membuktikan kita sudah menguasai seluruh fungsi Operator dan Ekspresi, mari kita buat sebuah mesin pengecek kelulusan beasiswa.

**Spesifikasi Tugas**:

- Buat variabel penampung nilai siswa: `nilai_ujian = 70` dan `kehadiran = 85`.
- Siswa tersebut ternyata mendapatkan nilai tambahan (_bonus_) karena aktif di kelas. Gunakan **Operator Assignment Gabungan** (`+=`) untuk menambahkan `nilai_ujian` sebanyak `10` poin.
- Buat variabel pengecek `lulus_beasiswa` menggunakan **Operator Logika**. Syarat lulus adalah:
  - Nilai ujian (setelah ditambah bonus) harus **lebih besar atau sama dengan `80` DAN**
  - Kehadiran harus **lebih besar dari** `80`.
- Cetak nilai hasil akhir ujian dan status kelulusan (True/False) ke layar menggunakan F-String.

**Jawaban:**

```python
nilai_ujian = 70
kehadiran = 85

nilai_ujian += 10

lulus_beasiswa = nilai_ujian >= 80 and kehadiran > 80

print(f"Nilai Ujiah Akhir: {nilai_ujian}")
print(f"Jumlah Kehadiran: {kehadiran}%")
print(f"Status Beasiswa: {lulus_beasiswa}")
```

```terminal
(.venv) bengs@Benkz:~/belajar-python$ python3 mini-projects/mini_project_3.py
Nilai Ujiah Akhir: 80
Jumlah Kehadiran: 85%
Status Beasiswa: True
(.venv) bengs@Benkz:~/belajar-python$
```

---

## BAB 4: Control Flow

### Bagian 1

**1. Tujuan Pembelajaran**

Di bab ini, kita akan belajar cara memberikan "otak" kepada program agar bisa mengambil keputusan sendiri berdasarkan kondisi tertentu, serta menyuruh asisten komputer melakukan pekerjaan yang berulang-ulang tanpa lelah.

**2. Penjelasan Konsep Utama: Percabangan (`if`, `elif`, `else`)**

Sejauh ini, semua program yang kita tulis berjalan lurus dari baris pertama ke baris terakhir. Namun di dunia nyata, sebuah aplikasi harus bisa membuat keputusan.

- **Apa itu Percabangan?** Ini adalah cara kita menyuruh Python mengeksekusi kode tertentu **hanya jika** sebuah kondisi terpenuhi (bernilai `true`).
- **Mengapa ini penting?** Bayangkan layar login. Jika _password_ benar, masuk ke _dashboard_. Jika salah, tampilkan pesan _error_. Tanpa percabangan, semua alur akan dieksekusi sekaligus.

**Sintaks Dasar**:

- `if` (**Jika**): Pintu pertama. Akan dicek paling awal.
- `elif` (**else if / Jika yang lain**): Pintu alternatif. Hanya dicek jika `if` di atasnya bernilai `False`. Kita bisa memakai banyak `elif`.
- `else` (**Selain itu**): Pintu terakhir. Akan langsung dieksekusi jika semua `if` dan `elif` di atasnya `False`. Tidak perlu menuliskan kondisi di `else`.

**3. Contoh Kode & Aturan Emas Indentasi**

Di Python, spasi di awal baris (**indentasi**) sangatlah krusial. Indentasi (biasanya 1 kali tombol _Tab_ atau 4 kali _Spasi_) digunakan untuk menandakan bahwa sebuah blok kode adalah "milik" dari `if` atau `else` diatasnya.

```python
umur = 20

# Perhatikan tanda titik dua (:) di akhir setiap kondisi
if umur < 13:
  print("Kamu adalah anak-anak.")  # Baris ini menjorok ke dalam (Indentasi)
elif umur < 18:
  print("Kamu adalah remaja")
else:
  print("Kamu sudah dewasa")
```

**4. Visualisasi & Analogi**

Bayangkan kita sedang berada di persimpangan jalan tol.

- Penjaga gerbang pertama (`if`) bertanya: "Apakah kamu membawa mobil truk?". Jika ya, kamu diarahkan ke jalur kiri. Jika tidak, kamu lanjut ke gerbang berikutnya.
- Penjaga gerbang kedua (`elif`) bertanya: "Apakah kamu membawa modil sedan?". Jika ya, ke lajur tengah.
- Jika tidak semuanya (`else`), kamu otomatis diarahkan ke jalur kanan.

**5. Kesalahan Umum & Best Practices**

- **Kesalahan 1 (IndentationError)**: Lupa memberikan spasi menjorok ke dalam setelah menulis `if`. Python akan bingung dan memunculkan _error_.
- **Kesalahan 2 (SyntaxError)**: Lupa menambahkan titik dua (`:`) di akhir baris `if`, `elif` atau `else`.
- **Best Practices**: Selalu pastikan kondisi yang paling spesifik dicek terlebih dahulu di posisi `if` teratas.

**Latihan Praktik BAB 4: Sistem Tiket Bioskop**

**Bagian 1**

**Spesifikasi Tugas:**

1.  Minta pengguna memasukkan umur mereka (gunakan `input()` dan jangan lupa ubah menjadi `int()`)
2.  Buat struktur percabangan (`if-elif-else`) untuk menentukan harga tiket:
    1.  Jika umur di bawah 12 tahun (kurang dari 12), harga tiket = Rp 25.000.
    2.  Jika umur dari 12 hingga 60 tahun, harga tiket = Rp. 50.000
    3.  Jika umur di atas 60 tahun (Lansia), harga tiket = Rp 35.000.
3.  Cetak harga tiket yang harus dibayar menggunakan F-string.

**Jawaban:**

```python
usia_pengguna = int(input("Masukkan usia Anda saat ini: "))

if usia_pengguna < 12:
  print(f"Usia Anda adalah {usia_pengguna} tahun, harga tiket Anda adalah: Rp 25.000")
elif usia_pengguna <= 60:
    print(f"Usia Anda adalah {usia_pengguna} tahun, harga tiket Anda adalah: Rp 50.000")
else:
  print(f"Usia Anda adalah {usia_pengguna} tahun, harga tiket Anda adalah: Rp 35.000")
```

```terminal
(.venv) bengs@Benkz:~/belajar-python$ python3 main.py
Masukkan usia Anda saat ini: 11
Usia Anda adalah 11 tahun, harga tiket Anda adalah: Rp 25.000
(.venv) bengs@Benkz:~/belajar-python$ python3 main.py
Masukkan usia Anda saat ini: 12
Usia Anda adalah 12 tahun, harga tiket Anda adalah: Rp 50.000
(.venv) bengs@Benkz:~/belajar-python$ python3 main.py
Masukkan usia Anda saat ini: 25
Usia Anda adalah 25 tahun, harga tiket Anda adalah: Rp 50.000
(.venv) bengs@Benkz:~/belajar-python$ python3 main.py
Masukkan usia Anda saat ini: 60
Usia Anda adalah 60 tahun, harga tiket Anda adalah: Rp 50.000
(.venv) bengs@Benkz:~/belajar-python$ python3 main.py
Masukkan usia Anda saat ini: 65
Usia Anda adalah 65 tahun, harga tiket Anda adalah: Rp 35.000
(.venv) bengs@Benkz:~/belajar-python$
```

### Bagian 2

**1. Tujuan Pembelajaran**

Kita akan belajar cara menyuruh asisten komputer melakukan tugas yang berulang-ulang secara otomatis dalam hitungan milidetik menggunakan konsep **perulangan (loops)**.

**2. Penjelasan Konsep Utama: Kenapa Butuh Perulangan?**

Bayangkan kita harus mencetak teks "Halo" sebanyak 100 kali. Menulis `print("Halo")` sebanyak 100 baris tentu sangat membuang waktu. Di sinilah _Loops_ berperan. Python memiliki dua jenis perulangan utama: `for` dan `while`.

**A. Perulangan `for` (Untuk jumlah yang sudah pasti)**

Digunakan ketika kita **sudah tahu persis** berapa kali sebuah tugas harus diulang. Di Python, `for` sering dikombinasikan dengan fungsi `range()`.

```python
# Akan mengulang sebanyak 5 kali (mulai dari 0, berhenti sebelum 5)
for i in range(5):
  print(f"Mengirim paket data ke-{i}")
```

_Catatan Penting: Di dunia pemrograman, komputer selalu mulai menghitung dari angka 0, bukan 1. Jadi `range(5)` akna menghasilkan angka: 0, 1, 2, 3, 4_.

**B. Perulangan `while` (Selama kondisi bernilai True)**

Digunakan ketikan kita **tidak tahu pasti** kapan perulangan harus berhenti, tetapi kamu tahu _syarat berhentinya_. Perulangan ini akan terus berjalan berputar-putar _selama_ kondisinya masih `True`.

**Visualisasi & Analogi**:

Bayangkan sebuah sistem _monitoring_ aplikasi.

- `for` **loop**: "Ping ke _server_ persis sebanyak 4 kali lalu laporkan hasilnya." (Jumlah tugas jelas)
- `while` **loop**: "Terus bunyikan alarm **selama** status _server_ masih _down_." (Kita tidak tahu kapan _server_ menyala, alarm hanya berhenti jika status berubah menjadi _up_).

```python
status_server = "Down"
detik = 1

# Akan terus berulang SELAMA statusnya "Down"
while status_server == "Down":
  print(f"Detik {detik}: Server masih mati, mencoba lagi...")
  detik += 1

  # Simulasi: pada detik ke-3, server akhirnya menyala
  if detik == 4:
    status_server = "Up"
    print("Server kembali online!")
```

**3. Penjelasan Konsep Utama: `break` dan `continue`**

Terkadang kita perlu menginterupsi perulangan di tengah jalan.

- `break`: Menghancurkan / menghentikan perulangan secara paksa saat itu juga, meskipun tugasnya belum selesai.
- `continue`: Melompati sisa kode putaran saat ini, dan langsung melompat ke putaran berikutnya.

```python
for angka in range(1, 6): # Dari 1 sampai 5
  if angka == 3:
    print("Angka 3 dilewati!")
    continue    # Lewati baris print di bawah ini, langsung lanjut ke 4

  print(f"Memproses angka {angka}")
```

**4. Kesalahan Umum**

- **Kesalahan (Infinite Loops)**: Saat menggunakan `while`, lupa mengubah kondisi menjadi `False`. Akibatnya, program berjalan selamanya sampai komputer _hang_ atau kehabisan memori.
- **Solusi**: Selalu pastikan ada mekanisme (seperti menambah variabel hitungan atau menggunakan `break`) agar perulangan `while` bisa berhenti. (Jika tidak sengaja terjebak _infinite loop_ di terminal, tekan `Ctrl + C` untuk memaksanya berhenti).

**Mini Project BAB 4: Sistem Login Terminal (Brute-Force Protection)**

Mari kita gabungkan `while`, `if-else` dan `break` ke dalam satu skenario dunia nyata.

**Spesifikasi Tugas:**

1.  Buat variabel `pin_rahasia` dengan nilai `"1234"`.
2.  Buat variabel kesempatan dengan nilai `3`.
3.  Gunakan perulangan `while` yang akan terus berjalan **selama** `kesempatan > 0.
4.  Di dalam perulangan, minta pengguna memasukkan PIN menggunakan `input()`.
5.  Buat percabangan:
    1.  **Jika PIN benar**: Cetak "Login Berhasil!", lalu gunakan `break` untuk keluar dari perulangan.
    2.  **Jika PIN salah**: kurangi variabel `kesempatan` sebanyak 1 (`kesempatan -= 1`), lalu cetak "PIN Salah. Kesempatan tersisa: [Jumlah_kesempatan]".
6.  **Di luar/setelah** perulangan `while`, buat pengecekan `if` satu kali lagi: jika `kesempatan == 0`, cetak "Akun Terblokir!".

Silakan pelajari logikanya pelan-pelan. Tulis kode dan jalankan di terminal. Uji dengan dua skenario:

1.  Skenario tebakan benar
2.  Skenario salah 3 kali berturut-turut sampai terblokir.

**Jawaban:**

```python
pin_rahasia = "090398"

kesempatan = 3

while kesempatan > 0:
  masukkan_pin = input("Masukkan PIN: ")

  if masukkan_pin == pin_rahasia:
    print(f"Login Berhasil!")
    break
  else:
    kesempatan -= 1
    print(f"PIN Salah. Kesempatan tersisa: {kesempatan}")

if kesempatan == 0:
  print("Akun Terblokir!")
```

```terminal
(.venv) bengs@Benkz:~/belajar-python$ python3 mini-projects/mini_project_4.py
Masukkan PIN: 090398
Login Berhasil!
(.venv) bengs@Benkz:~/belajar-python$ python3 mini-projects/mini_project_4.py
Masukkan PIN: 001100
PIN Salah. Kesempatan tersisa: 2
Masukkan PIN: 112233
PIN Salah. Kesempatan tersisa: 1
Masukkan PIN: 332211
PIN Salah. Kesempatan tersisa: 0
Akun Terblokir!
(.venv) bengs@Benkz:~/belajar-python$
```

---

## BAB 5: Fungsi (Functions)

### Bagian 1

**1. Tujuan Pembelajaran**

Di bab ini, kita akan belajar cara "membungkus" puluhan baris kode menjdadi satu alat praktis yang bisa kita panggil berulang kali tanpa harus mengetik kodenya dari nol. Ini adalah fondasi dari **Modularitas** (memcah program besar menjadi bagian-bagian kecil yang rapi).

**2. Penjelasan Konsep Utama: Apa itu Fungsi?**

Sejauh ini, setiap kali kita ingin melakukan sesuatu, kita menulis kode secara berurutan. Masalahnya, bagaimana jika di dalam aplikasi yang sama, kita butuh mengecek PIN _login_ di 5 halaman yang berbeda? Menulis ulang _looping_ `while` pengecekan PIN sebanyak 5 kali tentu sangat tidak efisien dan rentan terjadi kesalahan (_error_).

**Fungsi (Function)** adalah sekumpulan kode yang diberi nama khusus. Kode di dalamnya **tidak akan berjalan** sampai kita memanggil nama tersebut.

**Visualisasi & Analogi**:

Bayangkan sebuah **mesin pembuat jus**.

Kita tahu bahwa mesin itu bertugas menghancurkan buah menjadi minuman. Saat kita ingin membuat jus, kita tidak perlu merakit pisau dan motor dinamonya dari nol setiap kali. Kita cukup memasukkan buah (Input), menekan tombol "Blender" (Memanggil Fungsi), dan mesin akan mengeluarkan jusnya (Output).

Di Python, kita mendefinisikan fungsi menggunakan kata kunci `def` (singkatan dari _define_).

**Sintaks Dasar**:

```python
# 1. MENDOBRAK (Mendefinisikan) FUNGSI
def sapa_pengguna():
  print("Halo! Selamat datang di aplikasi kami.")
  print("Semoga harimu menyenangkan.")

# Kode di atas belum menghasilkan apa-apa di layar sampai kita memanggilnya

# 2. MEMANGGIL FUNGSI
sapa_pengguna()   # Memanggil mesin untuk bekerja
sapa_pengguna()   # Memanggil lagi untuk kedua kalinya
```

**3. Penjelsan Konsep Utama: Parameter dan Argument (Input Fungsi)**

Mesin jus tidak akan berguna jika kita tidak bisa memasukkan buah ke dalamnya. Sama halnya dengan fungsi. Kita bisa memberikan data (buah) ke dalam fungsi agar diproses. Data yang diterima oleh fungsi disebut **Parameter**.

```python
# 'nama' di dalam kurung adalah Parameter (seperti corong tempat masuk buah)
def sapa_personal(nama):
  print(f"Halo, pahlawan {nama}! Selamat bertugas.")

# Saat panggilan, kita memerikan Argument (buah yang sesungguhnya)
sapa_personal("Bengs")
sapa_personal("Andi")
```

**4. Kesalahan Umum & Best Practices**

- **Kesalahan**: Lupa menambahkan tanda kurung `()` saat memanggil fungsi. Jika kita hanya mengetik `sapa_personel` tanpa kurung, Python hanya akan memberi tahu bahwa itu adalah sebuah fungsi, tetapi tidak menjalankannya.
- **Best Practice**: Gunakan kata kerja untuk menamai fungsi, karena fungsi melakukan sebuah tindakan. Contoh yang baik: `hitung_total()`, `cek_kondisi()`, `simpan_data()`.

**Latihan Praktik BAB 5: Kalkulator Diskon Sederhana**

Mari kita uji pemahaman tentang pembuatan fungsi dasar beserta parameternya.

**Spesifikasi Tugas**:

1.  Buat sebuah fungsi bernama `hitung_diskon`.
2.  Fungsi tersebut harus bisa menerima dua input (parameter): `harga_asli` dan `persen_diskon`.
3.  Di dalam fungsi tersebut:
    1.  Hitung jumlah potongan harga dengan rumus matematika: `(persen_diskon / 100) * harga_asli`
    2.  Hitung harga akhir setelah didiskon: `harga_asli - potongan`
    3.  Cetak harga akhirnya menggunakan F-String, contoh: `"Harga setelah diskon adalah: Rp [harga_akhir]"`
4.  Di bagian bawah (di luar fungsi), **panggil fungsi tersebut dua kali** dengan data yang berbeda. Misalnya:
    1.  Barang pertama: harga 100.000, diskon 20%
    2.  Barang kedua: harga 50.000, diskon 10%

**Jawaban:**

```python
def hitung_diskon(harga_asli, persen_diskon):
  potongan_harga = (persen_diskon / 100) * harga_asli

  harga_akhir = harga_asli - potongan_harga

  print(f'Harga setelah diskon adalah: Rp {harga_akhir}')

hitung_diskon(100000, 20)
hitung_diskon(50000, 10)
```

```terminal
(.venv) bengs@Benkz:~/belajar-python$ python3 main.py
Harga setelah diskon adalah: Rp 80000.0
Harga setelah diskon adalah: Rp 45000.0
(.venv) bengs@Benkz:~/belajar-python$
```

### Bagian 2

**1. Tujuan Pembelajaran**

Di bagian ini, kita akan memahami perbedaan krusial antara sekedar mencetak hasil (`print`) versus "mengembalikan" hasil ke sistem (`return`), serta mamahami batasan wilayah memori (Scope) dari sebuah variabel.

**2. Penjelasan Konsep Utama: `return` vs `print()`**

Pada kodemu sebelumnya, fungsi `hitung_diskon` langsung mencetak harga ke layar menggunakan `print()`. Ini terlihat bagus, tapi **komputer tidak menyimpan hasil perhitungan itu**.

**Visualisasi & Analogi**:

Bayangkan kita menyuruh asisten kita (fungsi) pergi ke pasar membawa uang (Parameter/Input) untuk membeli apel.

- Jika menggunakan `print()`: Asisten kita membeli apel, memakannya sendiri di pasar, lalu menelepon kita: "_Bos, apelnya enak!_". Kita tahu hasilnya, tapi **kita tidak medapatkan apelnya ditangan kita** untuk diolah lagi menjadi jus.
- Jika menggunakan `return`: Asisten kita membeli apel, membawanya pulang dan **menyerahkannya ke tangan kita** (Output). Sekarang, kita bisa menyimpan apel itu di kulkas (Variabel) atau langsung memblendernya (Perhitungan lanjutan).

Di aplikasi nyata (seperti Tokopedia atau Shopee), sistem butuh hasil perhitungan diskon untuk dijumlahkan dengan ongkos kirim. Jika hanya di-`print`, sistem tidak bisa menjumlahkannya.

**Sintaks Dasar `return`**:

```python
def kalikan_dua(angka):
  hasil = hasil * 2
  return hasil    # Mengembalikan nilai ke pemanggilnya, BUKAN mencetaknya

# Karena fungsi ini mengembalikan nilai, kita bisa menyimpannya ke dalam kotak (varibel)
nilai_baru = kalikan_dua(10)

# Sekarang kita bisa menggunakan nilai itu untuk hal lain
print(f"Hasilnya jika ditambah 5 adalah: {nilai_baru + 5}")
```

_Catatan Penting: Saat Python membaca kata `return`, fungsi akan **langsung berhenti bekerja**. Kode apa pun yang ditulis di bawah baris `return` di dalam fungsi tersebut tidak akan pernah dieksekusi_.

**3. Penjelasan Konsep Utama: Ruang Lingkup Varibel (Scope)**

Kenapa kita tidak bisa langsung mengambil variabel `potongan_harga` dari kode sebelumnya? Karena varibel di Python memiliki "wilayah kekuasaan" (scope).

- **Local Scope**: Variabel yang dibuat **di dalam** fungsi (seperti `potongan_harga` dan `harga_akhir`) hanya hidup di dalam pabrik (fungsi) itu. Jalan raya (kode di luar fungsi) tidak tahu varibel itu ada.
- **Global Scope**: Varibel yang dibuat di luar fungsi (di baris paling kiri tanpa identitas) bisa dilihat oleh semua orang, termasuk oleh fungsi.

**Latihan Praktik BAB 5**

**Bagian 2**: **Sistem Keranjang Belanja**

Mari kita "tingkatkan" (refactor) fungsi yang sudah kita buat sebelumnya agar lebih bertaraf industri.

**Spesifikasi Tugas**:

- Ubah fungsi `hitung_diskon`. Hapus baris `print(...)` di dalamnya, dan ganti dengan printah untuk **mengembalikan** (`return`) nilai dari `harga_akhir`.
- Di luar fungsi, panggil fungsi tersebut untuk menghitung dua barang:
  - Sepatu: Harga 200.000, Diskon 15%
  - Baju: Harga 100.000, Diskon 50%
- **Simpan** hasil dari masing-masing pemanggilan fungsi tersebut ke dalam varibel baru (misal: `harga_sepatu` dan `harga_baju`).
- Buat varibel baru bernama `total_bayar` yang merupakan hasil penjumlahan `harga_sepatu` dan `harga_baju`.
- Terakhir, `print()` variabel `total_bayar` tersebut menggunakan f-string. (Misal: "_Total yang harus dibayar adalah Rp ..._")

**Jawaban:**

```python
# Latihan Praktik BAB 5: Bagian 2
def hitung_diskon(harga_asli, persen_diskon):
  potongan_harga = (persen_diskon / 100) * harga_asli

  harga_akhir = harga_asli - potongan_harga

  return harga_akhir

harga_sepatu = hitung_diskon(200000, 15)
harga_baju = hitung_diskon(100000, 50)
total_bayar = harga_sepatu + harga_baju

print(f"Total yang harus dibayarkan adalah Rp {total_bayar:,}")
```

```terminal
(.venv) bengs@Benkz:~/belajar-python$ python3 main.py
Total yang harus dibayarkan adalah Rp 220,000.0
(.venv) bengs@Benkz:~/belajar-python$
```

### Bagian 3

**1. Tujuan Pembelajaran**

Di bagian ini, kita akan belajar cara mendobrak batasan jumlah parameter. Kita akan membuat fungsi yang bisa menerima berapapun jumlah _input_ yang diberikan oleh pengguna, serta mengenal fungsi sebaris (_Lambda_).

**2. Penjelasan Konsep Utama: `*args` (Arguments)**

Pada kode sebelumnya, fungsi `hitung_diskon` meminta persis 2 parameter `(harga_asli, persen_diskon)`. Jika kita memasukkan 3 angka, program akan _error_.

Tapi bagaimana jiak kita ingin membuat alat `hitung_total_belanja()` dan kita tidak tahu apakah pelanggan akan membeli 1, 5 atau 100 barang?

Di sinilah `*args` berperan. Tanda bintang `*` di depan parameter adalah keajaibannya. Ia bertindak seperti "kantong belanja ajaib". Berapa pun jumlah data yang kita masukkan, Python akan membungkusnya ke dalam stau kantong tersebut.

**Contoh Kode**

```python
# Tanda * memberitahu Python: "Terima berapapun argumen yang masuk!"
def sapa_banyak_orang(*nama_orang):
  # Karena nama_orang sekarang adalah sebuah "kantong", kita bisa menggunakan loop
  for nama in nama_orang:
    print(f"Halo, {nama}!")

# Kita bisa memasukkan 1, 4, atau 100 nama tanpa error
sapa_banyak_orang("Bengs", "Andi", "Budi", "Siti")
```

(*Catatan industri: Kata `args` hanyalah kebiasaan/standar. Kita bebas menamainya `*nama_orang`, `_angka`, atau apa pun, selama ada tanda bintang di depannya_).

Ada juga pasangannya yaitu `*kwargs` (Keyword Arguments) dengan dua bintang. Ini digunakan jika data kita memiliki label (seperti `nama = "Bengs", umur = 28`). Namun, kita akan mendalaminya nanti di BAB 6 saat kita membahas struktur data _Dictionary_.

**3. Penjelasan Konsep Utama: Lambda (Fungsi Tanpa Nama)**

Kadang, di industri kita butuh fungsi matematika yang sangat sederhana dan hanya dipakai sekali. Terasa boros baris jika harus menulis blok `def` yang panjang. Python punya jalan pintas untuk membuat fungsi di dalam satu baris, yang disebut `lambda`.

```python
# 1. Menggunakan def (Cara biasa)
def kuadrat(x):
  return x * x

# 2. Menggunakan Lambda (Cara super singkat)
# Sintaks: variabel = lambda parameter : nilai_yang_di_return
kuadrat_cepat = lambda x: x * x

print(kuadrat_cepat(5))   # Hasilnya 25
```

**Latihan Praktik BAB 5: Kalkulator Keranjang Dinamis**

**Bagian 3**

Mari kita uji pemahaman tentang kantong ajaib `*args`. Ini sangat sering digunakan untuk membuat kalkulator data massal.

**Spesifiksi Tugas**:

1.  Buat sebuah fungsi bernama `jumlahkan_semua`.
2.  Fungsi ini hanya menerima satu parameter bertanda bintang (misalnya `*harga_barang`).
3.  Di dalam fungsi, buat variabel `total = 0`.
4.  Gunakan perulangan `for` untuk membedah isi `harga_barang`, dan tambahkan setiap harganya ke dalam variabel `total` (ingat materi operator `+=`?).
5.  Terakhir, `return` nilai `total` tersebut.
6.  Di luar fungsi, panggil fungsi tersebut dengan memasukkan **4 angka sembarang** (misal: 10000, 5000, 20000, 15000), simpan hasilnya di sebuah variabel, dan `print()` dengan rapi.

**Jawaban:**

```python
def jumlahkan_semua(*harga_barang):
  total = 0

  for harga in harga_barang:
    total += harga

  return total

hasil = jumlahkan_semua(10000, 5000, 20000, 15000)

print(f"Total harga semua barang: Rp {hasil:,}")
```

```terminal
(.venv) bengs@Benkz:~/belajar-python$ python3 main.py
Total harga semua barang: Rp 50,000
(.venv) bengs@Benkz:~/belajar-python$
```

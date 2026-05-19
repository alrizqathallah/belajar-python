# Program pertama
# print("Halo, dunia!")
# print("Saya siap membuat asisten otomatis.")

# Meminta asisten berkenalan
# nama_pengguna = input("Halo! Siapa namamu? ")
# makanan_favorit = input("Apa makanan favoritmu? ")
# print("Salam kenal,", nama_pengguna)
# print("Makanan favoritmu adalah", makanan_favorit)

# nama = "Bengs"          # Sting (str)
# umur = 28               # Integer (int)
# suhu = 36.7             # Float (float)
# sedang_belajar = True   # Boolean (bool)

# Menggunakan f-string (perhatikan huruf 'f' di depan tanda kutip)
# print(f"Halo, nama saya {nama} dan saya berumur {umur} tahun.")

# Mengecek tipe data
# print(type(suhu))

# Kalkulator Tahun Lahir
# nama_pengguna = input("Siapa nama Anda? ")
# tahun_lahir = input("Kapan tahun lahir Anda? ")
# umur_pengguna = 2026 - int(tahun_lahir)

# print(f"Halo {nama_pengguna}, umur anda adalah {umur_pengguna} tahun")

# Latihan Praktik
# teks_berantakan = "     bENgs "
# teks_bersih = teks_berantakan.strip().title()     # Menghapus spasi DULU, lalu membuat awalan kapital

# print(f"Hasil sebelum dibersihkan: '{teks_berantakan}'")
# print(f"Hasil sebelum dibersihkan: '{teks_bersih}'")

# Latihan Praktik
jumlah_hari = 45
pekan = jumlah_hari // 7
sisa_hari = jumlah_hari % 7
cek_sisa = sisa_hari == 3

print(f"Jumlah hari      : {jumlah_hari}")
print(f"Minggu penuh     : {pekan}")
print(f"Sisa hari        : {sisa_hari}")
print(f"Apakah sisa = 3? : {cek_sisa}")
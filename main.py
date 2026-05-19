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
# jumlah_hari = 45
# pekan = jumlah_hari // 7
# sisa_hari = jumlah_hari % 7
# cek_sisa = sisa_hari == 3

# print(f"Jumlah hari      : {jumlah_hari}")
# print(f"Minggu penuh     : {pekan}")
# print(f"Sisa hari        : {sisa_hari}")
# print(f"Apakah sisa = 3? : {cek_sisa}")

# Latihan Praktik Bab 4
# usia_pengguna = int(input("Masukkan usia Anda saat ini: "))

# if usia_pengguna < 12:
#   print(f"Usia Anda adalah {usia_pengguna} tahun, harga tiket Anda adalah: Rp 25.000")
# elif usia_pengguna <= 60:
#     print(f"Usia Anda adalah {usia_pengguna} tahun, harga tiket Anda adalah: Rp 50.000")
# else:
#   print(f"Usia Anda adalah {usia_pengguna} tahun, harga tiket Anda adalah: Rp 35.000")

# Latihan Praktik BAB 5: Bagian 1
# def hitung_diskon(harga_asli, persen_diskon):
#   potongan_harga = (persen_diskon / 100) * harga_asli
  
#   harga_akhir = harga_asli - potongan_harga
  
#   print(f'Harga setelah diskon adalah: Rp {harga_akhir}')
  
# hitung_diskon(100000, 20)
# hitung_diskon(50000, 10)

# Latihan Praktik BAB 5: Bagian 2
# def hitung_diskon(harga_asli, persen_diskon):
#   potongan_harga = (persen_diskon / 100) * harga_asli
  
#   harga_akhir = harga_asli - potongan_harga
  
#   return harga_akhir
  
# harga_sepatu = hitung_diskon(200000, 15)
# harga_baju = hitung_diskon(100000, 50)
# total_bayar = harga_sepatu + harga_baju

# print(f"Total yang harus dibayarkan adalah Rp {total_bayar:,}")

# Latihan BAB 5: Bagian 3
def jumlahkan_semua(*harga_barang):
  total = 0
  
  for harga in harga_barang:
    total += harga
    
  return total

hasil = jumlahkan_semua(10000, 5000, 20000, 15000)

print(f"Total harga semua barang: Rp {hasil:,}")
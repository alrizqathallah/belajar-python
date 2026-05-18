nama_lengkap = input("Halo, siapa namamu? ")
tahun_lahir = input("Tahun berapa kamu lahir? ")
tinggi_cm = input("Berapa tinggi badan mu? ")

nama_diperbaiki = nama_lengkap.strip().title()
umur_pasti = 2026 - int(tahun_lahir)
tinggi_m = float(tinggi_cm) / 100

print(f"Halo {nama_diperbaiki}, umurmu {umur_pasti} tahun dan tinggi badanmu {tinggi_m} meter")
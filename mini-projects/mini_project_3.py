nilai_ujian = 70
kehadiran = 85

nilai_ujian += 10

lulus_beasiswa = nilai_ujian >= 80 and kehadiran > 80

print(f"Nilai Ujiah Akhir: {nilai_ujian}")
print(f"Jumlah Kehadiran: {kehadiran}%")
print(f"Status Beasiswa: {lulus_beasiswa}")
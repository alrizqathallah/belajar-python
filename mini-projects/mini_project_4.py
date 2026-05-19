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
  
statusKeanggotaan = input("Masukkan Status Keanggotan Anda:")
if statusKeanggotaan == "gold" or statusKeanggotaan == "silver":
    print("Selamt! Anda mendapatkan diskon")
elif statusKeanggotaan == "bronze":
    print("Anda tidak mendapatkan diskon")
else:
    print("Inputan yang anda masukkan tidak valid")
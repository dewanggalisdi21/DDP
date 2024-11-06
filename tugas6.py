import math

def hitung_luas():
    print("Pilih bangun datar:")
    print("1. Persegi")
    print("2. Lingkaran")
    print("3. Segitiga")

    pilihan = int(input("Masukkan pilihan (1/2/3): "))

    match pilihan:
        case 1:
            # Luas Persegi: sisi * sisi
            sisi = float(input("Masukkan panjang sisi persegi: "))
            luas = sisi * sisi
            print(f"Luas Persegi: {luas} unit²")
        
        case 2:
            # Luas Lingkaran: π * r * r
            jari_jari = float(input("Masukkan jari-jari lingkaran: "))
            luas = math.pi * jari_jari * jari_jari
            print(f"Luas Lingkaran: {luas:.2f} unit²")
        
        case 3:
            # Luas Segitiga: 1/2 * alas * tinggi
            alas = float(input("Masukkan panjang alas segitiga: "))
            tinggi = float(input("Masukkan tinggi segitiga: "))
            luas = 0.5 * alas * tinggi
            print(f"Luas Segitiga: {luas} unit²")
        
        case _:
            print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")

# Panggil fungsi untuk menghitung luas
hitung_luas()

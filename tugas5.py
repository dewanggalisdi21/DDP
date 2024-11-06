# Daftar kendaraan
kendaraan = [
    {
        "nama": "Honda Civic",
        "jenis": "Mobil",
        "cc": 1800,
        "warna": "Hitam",
        "roda": 4
    },
    {
        "nama": "Yamaha R15",
        "jenis": "Motor",
        "cc": 150,
        "warna": "Biru",
        "roda": 2
    },
    {
        "nama": "Suzuki Ertiga",
        "jenis": "Mobil",
        "cc": 1500,
        "warna": "Putih",
        "roda": 4
    },
    {
        "nama": "Kawasaki Ninja",
        "jenis": "Motor",
        "cc": 250,
        "warna": "Hijau",
        "roda": 2
    }
]

# Cetak daftar kendaraan
for k in kendaraan:
    print(f"Nama: {k['nama']}, Jenis: {k['jenis']}, CC: {k['cc']}, Warna: {k['warna']}, Roda: {k['roda']}")

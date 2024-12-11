from Animal import *

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, paruh, terbang):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.paruh = paruh
        self.terbang = terbang

    def cetak_burung(self):
        super().cetak()
        print("paruh \t\t\t\t:", self.paruh,
        "\nterbang \t\t\t:", self.terbang)

tukan = Burung("Tukan", "buah", "amerika tengah", "bertelur", "besar", "bisa terbang")
tukan.cetak_burung()
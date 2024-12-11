from Animal import *

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, design, mulut):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.design = design
        self.mulut = mulut

    def cetak_ikan(self):
        super().cetak()
        print("design \t\t\t\t:", self.design,
        "\nmulut \t\t\t\t:", self.mulut)

arapaima = Ikan("Arapaima", "ikan kecil", "amazon", "bertelur", "merah", "berukuran besar")
arapaima.cetak_ikan()
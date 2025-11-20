class Dosen:
    def __init__(self, nama, nidn):
        self.nama = nama
        self.nidn = nidn

    def ajar_mata_kuliah(self, mata_kuliah):
        return f"Saya Dosen {self.nama} (NIDN: {self.nidn}) mengajar mata kuliah {mata_kuliah}"

dosen1 = Dosen("Ir. Abadi Nugroho, S.Kom., M.Kom", "1104129002")
dosen2 = Dosen("Lapu' Tombilayuk, S.Kom., M.T.", "1120107301")

print(dosen1.ajar_mata_kuliah("Sistem Basis Data"))
print(dosen2.ajar_mata_kuliah("Sistem Informasi"))
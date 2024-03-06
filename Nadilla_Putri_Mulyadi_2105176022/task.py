class Mahasiswa:
    def __init__(self, nama, kelas, prodi, fakultas, tempat_tinggal, asal):
        self.nama = nama
        self.kelas = kelas
        self.prodi = prodi
        self.fakultas = fakultas
        self.tempat_tinggal = tempat_tinggal
        self.asal = asal

    def display_info(self):
        print("Nama:", self.nama)
        print("Kelas:", self.kelas)
        print("Program Studi:", self.prodi)
        print("Fakultas:", self.fakultas)
        print("Tempat Tinggal:", self.tempat_tinggal)
        print("Asal:", self.asal)

# Contoh penggunaan:
mahasiswa1 = Mahasiswa("Nadilla Putri Mulyadi", "A Pendidikan Komputer 2021", "Pendidikan Komputer", "FKIP", "Tanah Grogot", "Kabupaten Paser")
mahasiswa1.display_info()
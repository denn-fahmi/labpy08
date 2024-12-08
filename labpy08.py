class DaftarNilai:
    def __init__(self):
        self.daftar_nilai = {}

    def tambah(self):
        nama = input("Masukkan nama mahasiswa: ")
        nilai = float(input("Masukkan nilai mahasiswa: "))
        self.daftar_nilai[nama] = nilai
        print(f"Data mahasiswa {nama} berhasil ditambahkan.\n")

    def tampilkan(self):
        if not self.daftar_nilai:
            print("Daftar nilai masih kosong.\n")
        else:
            print("\nDaftar Nilai Mahasiswa:")
            print("=" * 25)
            print(f"{'Nama':<15}{'Nilai':>10}")
            print("=" * 25)
            for nama, nilai in self.daftar_nilai.items():
                print(f"{nama:<15}{nilai:>10.2f}")
            print("=" * 25 + "\n")

    def hapus(self):
        nama = input("Masukkan nama mahasiswa yang ingin dihapus: ")
        if nama in self.daftar_nilai:
            del self.daftar_nilai[nama]
            print(f"Data mahasiswa {nama} berhasil dihapus.\n")
        else:
            print("Data mahasiswa tidak ditemukan.\n")

    def ubah(self):
        nama = input("Masukkan nama mahasiswa yang ingin diubah nilainya: ")
        if nama in self.daftar_nilai:
            nilai_baru = float(input("Masukkan nilai baru: "))
            self.daftar_nilai[nama] = nilai_baru
            print(f"Data nilai mahasiswa {nama} berhasil diubah.\n")
        else:
            print("Data mahasiswa tidak ditemukan.\n")

def main():
    daftar_nilai = DaftarNilai()
    
    while True:
        print("Menu Utama:")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Hapus Data")
        print("4. Ubah Data")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == '1':
            daftar_nilai.tambah()
        elif pilihan == '2':
            daftar_nilai.tampilkan()
        elif pilihan == '3':
            daftar_nilai.hapus()
        elif pilihan == '4':
            daftar_nilai.ubah()
        elif pilihan == '5':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid!\n")

if __name__ == "__main__":
    main()

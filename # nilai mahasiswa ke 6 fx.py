# Program Sederhana Manajemen Nilai Mahasiswa

# Struktur data untuk menyimpan data mahasiswa
# List of Dictionaries: [{'nama': 'Budi', 'nilai': 85}, {'nama': 'Ani', 'nilai': 90}]
data_mahasiswa = []


## 🛠️ Fungsi Utama Program

### Fungsi 1: tambah()
def tambah():
    """Menambahkan data mahasiswa (nama dan nilai) ke dalam list."""
    print("\n--- Tambah Data Mahasiswa ---")
    nama = input("Masukkan Nama Mahasiswa: ").strip()

    # Cek apakah nama sudah ada
    for mhs in data_mahasiswa:
        if mhs['nama'].lower() == nama.lower():
            print(f"❌ Error: Mahasiswa dengan nama '{nama}' sudah ada.")
            return

    try:
        nilai = float(input("Masukkan Nilai Mahasiswa (0-100): "))
        if not (0 <= nilai <= 100):
            print("❌ Error: Nilai harus antara 0 sampai 100.")
            return
    except ValueError:
        print("❌ Error: Input nilai tidak valid (harus angka).")
        return

    # Menambahkan data baru
    data_baru = {'nama': nama, 'nilai': nilai}
    data_mahasiswa.append(data_baru)
    print(f"✅ Sukses: Data '{nama}' dengan nilai {nilai} berhasil ditambahkan.")


### Fungsi 2: tampilkan()
def tampilkan():
    """Menampilkan semua data mahasiswa yang tersimpan."""
    print("\n--- Daftar Nilai Mahasiswa ---")
    if not data_mahasiswa:
        print("Tidak ada data mahasiswa yang tersimpan.")
        return

    # Menghitung panjang kolom maksimum untuk format tabel yang rapi
    max_nama = max(len(mhs['nama']) for mhs in data_mahasiswa) if data_mahasiswa else 4

    # Header Tabel
    print("-" * (max_nama + 15))
    print(f"| {'No.':<4} | {'Nama':<{max_nama}} | {'Nilai':<5} |")
    print("-" * (max_nama + 15))

    # Isi Tabel
    for i, mhs in enumerate(data_mahasiswa):
        print(f"| {i + 1:<4} | {mhs['nama']:<{max_nama}} | {mhs['nilai']:<5.2f} |")

    print("-" * (max_nama + 15))


### Fungsi 3: hapus(nama)
def hapus(nama):
    """Menghapus data mahasiswa berdasarkan nama."""
    print(f"\n--- Hapus Data Mahasiswa: {nama} ---")
    nama_lower = nama.lower()

    # Mencari dan menghapus data
    for i, mhs in enumerate(data_mahasiswa):
        if mhs['nama'].lower() == nama_lower:
            del data_mahasiswa[i]
            print(f"✅ Sukses: Data '{nama}' berhasil dihapus.")
            return

    # Jika nama tidak ditemukan
    print(f"❌ Error: Mahasiswa dengan nama '{nama}' tidak ditemukan.")


### Fungsi 4: ubah(nama)
def ubah(nama):
    """Mengubah data (nilai) mahasiswa berdasarkan nama."""
    print(f"\n--- Ubah Nilai Mahasiswa: {nama} ---")
    nama_lower = nama.lower()

    # Mencari data mahasiswa
    for mhs in data_mahasiswa:
        if mhs['nama'].lower() == nama_lower:
            try:
                nilai_baru = float(input(f"Masukkan Nilai Baru untuk '{mhs['nama']}' (0-100): "))
                if not (0 <= nilai_baru <= 100):
                    print("❌ Error: Nilai harus antara 0 sampai 100.")
                    return
            except ValueError:
                print("❌ Error: Input nilai tidak valid (harus angka).")
                return

            # Melakukan perubahan
            mhs['nilai'] = nilai_baru
            print(f"✅ Sukses: Nilai '{mhs['nama']}' berhasil diubah menjadi {nilai_baru}.")
            return

    # Jika nama tidak ditemukan
    print(f"❌ Error: Mahasiswa dengan nama '{nama}' tidak ditemukan.")


## 🖥️ Menu Utama Program
def menu_utama():
    """Menampilkan menu dan menjalankan fungsi sesuai pilihan pengguna."""
    while True:
        print("\n==============================")
        print("  SISTEM MANAJEMEN NILAI (CRUD)")
        print("==============================")
        print("1. Tambah Data (tambah())")
        print("2. Tampilkan Data (tampilkan())")
        print("3. Hapus Data (hapus(nama))")
        print("4. Ubah Data (ubah(nama))")
        print("5. Keluar")
        print("------------------------------")

        pilihan = input("Masukkan pilihan (1-5): ")

        if pilihan == '1':
            tambah()
        elif pilihan == '2':
            tampilkan()
        elif pilihan == '3':
            nama_hapus = input("Masukkan Nama Mahasiswa yang ingin dihapus: ").strip()
            if nama_hapus:
                hapus(nama_hapus)
            else:
                print("Nama tidak boleh kosong.")
        elif pilihan == '4':
            nama_ubah = input("Masukkan Nama Mahasiswa yang ingin diubah nilainya: ").strip()
            if nama_ubah:
                ubah(nama_ubah)
            else:
                print("Nama tidak boleh kosong.")
        elif pilihan == '5':
            print("Terima kasih. Program selesai.")
            break
        else:
            print("❌ Pilihan tidak valid. Silakan coba lagi.")


# Memulai program
if __name__ == "__main__":
    menu_utama()
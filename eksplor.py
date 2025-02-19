# Membuat dictionary mahasiswa
mahasiswa = {
    "nama": "Naruto",
    "nim": "12345",
    "jurusan": "Informatika",
    "angkatan": 2025
}

# 1. Menampilkan seluruh isi dictionary
print("Data Mahasiswa:", mahasiswa)

# 2. Mengakses nilai berdasarkan kunci
print("Nama Mahasiswa:", mahasiswa["nama"])
print("Jurusan Mahasiswa:", mahasiswa["jurusan"])

# 3. Menambahkan data baru ke dalam dictionary
mahasiswa["ipk"] = 3.75
print("Data Mahasiswa setelah ditambahkan IPK:", mahasiswa)

# 4. Mengubah data yang sudah ada
mahasiswa["jurusan"] = "Sistem Informasi"
print("Data Mahasiswa setelah jurusan diubah:", mahasiswa)

# 5. Menghapus salah satu data berdasarkan kunci
del mahasiswa["angkatan"]
print("Data Mahasiswa setelah menghapus angkatan:", mahasiswa)

# 6. Menampilkan semua kunci dan nilai dalam dictionary
print("Daftar Kunci:", mahasiswa.keys())
print("Daftar Nilai:", mahasiswa.values())
print("Daftar Item (key-value):", mahasiswa.items())

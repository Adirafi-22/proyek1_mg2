# Program Input dan Output
nama = input("Masukkan nama Anda: ")
umur = int(input("Masukkan umur Anda: "))
print(f"Halo, {nama}! Dua tahun lagi Anda akan berumur {umur + 2} tahun.")

 #Program menggunakan operator
a = 20
b = 2
print(f"Penjumlahan: {a + b}")
print(f"Pengurangan: {a - b}")
print(f"Perkalian: {a * b}")
print(f"Pembagian: {a / b}")

# Program contoh operator perbandingan

a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))

print(f"{a} == {b} : {a == b}")   # Sama dengan
print(f"{a} != {b} : {a != b}")   # Tidak sama dengan
print(f"{a} > {b}  : {a > b}")    # Lebih besar dari
print(f"{a} < {b}  : {a < b}")    # Lebih kecil dari
print(f"{a} >= {b} : {a >= b}")   # Lebih besar atau sama dengan
print(f"{a} <= {b} : {a <= b}")   # Lebih kecil atau sama dengan


# Program pengkondisian sederhana
nilai = int(input("Masukkan nilai: "))
if nilai >= 80:
    print("Grade: A")
elif nilai >= 70:
    print("Grade: B")
elif nilai >= 60:
    print("Grade: C")
else:
    print("Grade: D")

    # Daftar nilai siswa
nilai_siswa = [85, 60, 72, 90, 45, 78, 55, 88, 95, 67]

# Variabel untuk menghitung jumlah siswa yang lulus
jumlah_lulus = 0

# Loop untuk mengecek setiap nilai siswa
for nilai in nilai_siswa:
    print(f"Nilai siswa: {nilai}")
    
    # Cek apakah siswa lulus
    if nilai >= 70:
        jumlah_lulus += 1  # Tambah 1 jika lulus

# Menampilkan jumlah siswa yang lulus
print(f"Jumlah siswa yang lulus: {jumlah_lulus} dari {len(nilai_siswa)} siswa.")



# Daftar nilai siswa
nilai_siswa = [85, 60, 72, 90, 45, 78, 55, 88, 95, 67]

# Variabel untuk menghitung jumlah siswa yang lulus
jumlah_lulus = 0

# Indeks awal untuk iterasi
i = 0

# Loop while untuk mengecek setiap nilai siswa
while i < len(nilai_siswa):
    nilai = nilai_siswa[i]
    print(f"Nilai siswa: {nilai}")
    
    # Cek apakah siswa lulus
    if nilai >= 70:
        jumlah_lulus += 1  # Tambah 1 jika lulus
    
    # Increment indeks
    i += 1

# Menampilkan jumlah siswa yang lulus
print(f"Jumlah siswa yang lulus: {jumlah_lulus} dari {len(nilai_siswa)} siswa.")



# List nama buah
buah = ["Apel", "Mangga", "Jeruk", "Pisang", "Semangka"]

# 1. Cetak semua nama buah
print("Daftar buah:")
for b in buah:
    print(b)

# 2. Tampilkan jumlah buah dalam daftar
print(f"\nJumlah buah dalam daftar: {len(buah)}")

# 3. Ubah nama buah menjadi huruf besar
buah_upper = [b.upper() for b in buah]
print("\nNama buah dalam huruf besar:", buah_upper)

# 4. Cek apakah buah tertentu ada dalam daftar
cari = input("\nMasukkan nama buah yang ingin dicari: ")
if cari in buah:
    print(f"{cari} ada dalam daftar!")
else:
    print(f"{cari} tidak ditemukan dalam daftar.")

# 5. Gabungkan semua nama buah menjadi satu string
buah_string = ", ".join(buah)
print("\nBuah dalam satu string:", buah_string)



# Daftar angka
angka = [12, 45, 78, 23, 89, 34, 56, 91, 10, 67]

# 1. Menampilkan semua angka dalam list
print("Daftar angka:", angka)

# 2. Menampilkan jumlah elemen dalam list
print("Jumlah elemen dalam list:", len(angka))

# 3. Menampilkan angka terbesar dan terkecil
print("Angka terbesar:", max(angka))
print("Angka terkecil:", min(angka))

# 4. Mengurutkan list dalam urutan naik (ascending)
angka.sort()
print("List setelah diurutkan (ascending):", angka)

# 5. Mengurutkan list dalam urutan turun (descending)
angka.reverse()
print("List setelah diurutkan (descending):", angka)


# Membuat tuple angka
angka_tuple = (10, 25, 30, 45, 30, 60, 75, 30, 90)

# 1. Menampilkan isi tuple
print("Isi tuple:", angka_tuple)

# 2. Menampilkan jumlah elemen dalam tuple
print("Jumlah elemen dalam tuple:", len(angka_tuple))

# 3. Menampilkan angka terbesar dan terkecil dalam tuple
print("Angka terbesar:", max(angka_tuple))
print("Angka terkecil:", min(angka_tuple))

# 4. Mengakses elemen berdasarkan indeks
print("Elemen pertama:", angka_tuple[0])
print("Elemen terakhir:", angka_tuple[-1])

# 5. Mengiris (slicing) tuple
print("Elemen dari indeks 2 sampai 5:", angka_tuple[2:6])

# 6. Menghitung jumlah kemunculan angka 30 dalam tuple
print("Jumlah angka 30 dalam tuple:", angka_tuple.count(30))

# 7. Mencari indeks pertama dari angka 30 dalam tuple
print("Indeks pertama dari angka 30:", angka_tuple.index(30))








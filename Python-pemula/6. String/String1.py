#Print Hello World
print("Belajar String Pt.1")
print("1. Print Hello World")
print ("Hello World!")
print("===============")

#Print Hello World With Enter
print("2. Print Hello World Dengan Enter")
print("Hello")
print("World!")
print("===============")

#\n berfungsi untuk memisahkan kata Hello dan Word dengan enter atau garis baru
print("3. Memisahkan Hello World Dengan backslash + n")
print("Hello\nWorld!") 
print("===============")

#Memasukan String Kedalam Variabel dan Memanggil String Yang Ditampung oleh Variabel
print("4. Menambahkan String Kedalam Variabel dan Menampilkan Isi String Didalam Variabel")
a = "Hello World"
print(a)
print("===============")

#Menjumlahkan String
print("5. Menjumlahkan String")
a = "Hello"
b = "World"
c = a + " " + b
print(c)
print("===============")

#Mendapatkan karakter pertama dari string, (Urutan string dumulai dari 0)
print("6. Mendapatkan Karakter pertama dari String")
a = "Hello World"
print(a)
print("Karakter pertama dari Hello World yaitu :")
print(a[1])
print("===============")

#Penguraian String
print("7. Penguraian String")
for x in "Hello":
    print(x)
print("===============")

#Menghitung jumlah Panjang String
print("8. Menghitung Jumlah Panjang String")
a = "Hello World!"
print("Jumlah string dalam kata Hello World yaitu:")
print(len(a))
print("===============")

#Pengecekan String
print("9. Pengecekan String")
txt = "DKI Jakarta merupakan Ibu Kota Negara Indonesia"
print("Apakah kata Ibu ada didalam Kalimat : " + txt + "?")
print("Ibu" in txt)
print("===============")

#Pengecekan String Menggunakan IF
print("10. Pengecekan String Menggunakan IF")
txt = "DKI Jakarta merupakan Ibu Kota Negara Indonesia"
print("Apakah kata Ibu ada didalam Kalimat : " + txt + "?")
if ("Ibu" in txt) :
    print("Kata Ibu ada didalam kalimat " +"'" + txt + "'")
print("===============")

#Pengecekan Kata yang tidak ada dalam String
print("11. Pengecekan Kata Yang Tidak Ada Dalam String")
txt = "DKI Jakarta merupakan Ibu Kota Negara Indonesia"
print("Apakah kata Ibu ada didalam Kalimat : " + txt + "?")
print("Ayah" in txt)
print("===============")

#Pengecekan Kata yang tidak ada dalam String 2
print("12. Pengecekan Kata yang tidak ada dalam String (IF)")
txt = "DKI Jakarta merupakan Ibu Kota Negara Indonesia"
print("Apakah kata Ibu ada didalam Kalimat : " + txt + "?")
if ("Ayah" not in txt) :
    print("Kata Ayah tidak ada didalam kalimat " +"'" + txt + "'" + "silahkan cari kembali")
print("===============")
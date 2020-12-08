#Menggunakan Method format() untuk menambahkan angka kedalam string
print("1. Menggunakan Method format() untuk menambahkan angka kedalam string")
umur = 24
txt = "Nama saya Hadi Nurhidayat, dan umur saya {}"
print(umur)
print(txt + " >> Sebelum ditambahkan method format()")
print(txt.format(umur) + " >> Sesudah ditambahkan method format()")
print("===============================================================")

#Metode format () menggunakan jumlah argumen yang tidak terbatas, dan ditempatkan ke dalam placeholder masing-masing:
print("2. Menggunakan Method format() untuk menambahkan angka kedalam string")
kuantitas = 3
namabarang = "Indomie"
harga = 10000
pesanan = "Anda memesan {} sebanyak {} bungkus dengan harga Rp.{}"
txt1 = "Jumlah barang = {}" 
txt2 = "Nama barang yang dibeli = {}" 
txt3 = "Total harga Rp.{}"
print(txt1.format(kuantitas))
print(txt2.format(namabarang))
print(txt3.format(harga))
print(pesanan + " >> Sebelum ditambahkan method format()")
print(pesanan.format(namabarang,kuantitas,harga) + " >> Sesudah ditambahkan method format()")
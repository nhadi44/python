#Menggunakan Method Upper() Untuk Menghasilkan String Upper Case
print("1. Menggunakan Method Upper() Untuk Menghasilkan String Upper Case")
a = "Hello World"
print(a.upper())
print("===============================================================")

#Menggunakan Methon lower() Untuk Menghasilkan String Lower Case
print("2. Menggunakan Method Upper() Untuk Menghasilkan String Lower Case")
a = "Hello World"
print(a.lower())
print("===============================================================")

#Menghilangkan Whitespace Menggunakan Method strip()
print("3. Menghilangkan Whitespace Dari Bagian Awal atau Akhir Kalimat Menggunakan Method strip()")
a = " Hello World "
print(a)
print(a.strip())
print("===============================================================")

#The split() method returns a list where the text between the specified separator becomes the list items.
print("4. Method Split() mengembalikan ke dalam bentuk list")
a = "Hello, World!"
print(a)
print(a.split(",")) # returns ['Hello', ' World!']
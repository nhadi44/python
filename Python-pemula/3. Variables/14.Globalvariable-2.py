#Tetapi jika menggunakan keyword global, maka variabel akan selamanya menjadi global scope.
def MyName():
    global nama
    nama = "Hadi Nurhidayat"
MyName()
print("Nama saya " + nama)

#Untuk mengubah nilai variabel global di dalam fungsi, lihat variabel dengan menggunakan kata kunci global:
nama = "Hadi Nurhidayat"

def MyName():
    global nama
    nama = "Regina Wardani"
MyName()
print("Nama saya menjadi " + nama)
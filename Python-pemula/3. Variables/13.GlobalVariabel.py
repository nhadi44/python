#Membuat variabel diluar function dan gunakan variabel tersebut didalam function. Contoh
a = "Hadi Nurhidayat"

def myName():
    print("Nama saya"+" "+a)
myName()
print("================================================================================================")
print("================================================================================================")
"""
Jika Anda membuat variabel dengan nama yang sama di dalam fungsi, 
variabel ini akan menjadi variabel lokal, dan hanya dapat digunakan di dalam fungsi. 
Variabel global dengan nama yang sama akan tetap seperti sebelumnya, global dan dengan nilai aslinya
"""
nama = "Hadi Nurhidayat"
def nameMy():
    nama = "Regina Wardani"
    print("Nama saya" + " " + nama)
nameMy()
print("Nama saya" + " " + nama)
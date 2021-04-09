#program menghitung nilai rata-rata
#input
nilai = int(input("Masukkan banyak data: "))
data = []
n = 1
for n in range (0,nilai):
    angka = float(input("Masukkan data ke-{} :".format(n+1)))
    data.append(float(angka))
    n += 1

#output
rata_rata = sum(data)/nilai
print("Nilai Rata-rata: ",rata_rata)
print("Nama = lukmanul hakim")
print("Nim = A11.2016.09732")
print("Kelas = A11.54301")

x1 = 95
x2 = 175
n1 = 300
n2 = 280
a1 = -1.96
a2 = 1.96

print("Hipotesis H0 p1 = p2")
print("          H0 p1 != p2")
print("Derajat kebebasan 0.05 = 5% = a1 = ",a1,"-> a2 = ",a2,"-> Uji dua arah")
print("Daerah kritis H0 ditolak jika Z <",a1,"atau Z >",a2,)
print("Diket : x1 = 95  n1 = 300")
print("        x2 = 175  n2 = 280")


p = ((x1+x2)/(n1+n2))
q = 1 - p
print("p = ((x1+x2)/(n1+n2))")
print("Hasil dari p =",p,)
print("q = 1 - p")
print("Hasil dari q =",q,)
print("z = ((x1/n1)-(x2/n2))/(akar(p*q[((1/n1)+(1/n2))]))")
print("Hasil dari akar(p*q[((1/n1)+(1/n2))]) = 0.0411")


z = (((x1/n1)-(x2/n2))/0.0411)
z1 = 1.8945
print("Hasil dari z =",z,"Dikonver dengan table t -> z =",z1)
print("nialai Z = 1.65 > -1.96")
print("nialai Z = 1.65 < 1.96")
print("Kesimpulan")
print("Karena H0 berada di daerah tidak di terima dengan tingkat signifikasi 0.05 berarti proporsi populasi 2 kelurahan")





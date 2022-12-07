#belajar object dan class

class dodo: 
    warna = None
    usia = None
    
class kimnaldo:
    merk = None
    kecepatan = None

#membuat instance/fariable sebagai "objek nyata"
bangdo1 = dodo()
bangdo1.warna = "Black"
bangdo1.usia = "7"

bangdo2 = dodo()
bangdo2.warna = "White"
bangdo2.usia = "5"

portugal1 = dodo()
portugal1 = kimnaldo()
portugal1.warna = "Merah"
portugal1.bangsa = "Portugal"
portugal1.nomor = "7"

print (portugal1.warna)
print (portugal1.bangsa)
print (portugal1.nomor)
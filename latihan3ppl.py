# membuat variabel atau boc bernama buah

buah = [
    "Apel", "Anggur", "Pisang", "Alpukat", "Melon"
]

sayur = [
    "Pare", "Toge", "Kangkung", "Seledri", "Capcay"
]

dagang = buah + sayur
print (dagang)

for grobak in dagang:
    print (grobak)
    
    
kasir = input("Apalagi Coy ? :")
buah.append(kasir)
print(buah)
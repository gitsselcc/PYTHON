secuencia = "GCTCGACGATCGAT"
for i,base in enumerate(secuencia):
    print(f"Posicion {i} : {base}")

    #funcion sip
print("=========================")
bases = "ATGC"
complementos= "TACG"

for bases, complementos in zip(bases, complementos):
     print (f"La base es {base} y su complemento es {complementos}")
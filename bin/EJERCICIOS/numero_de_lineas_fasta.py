inputfile= "dna_sequences.fa"

with open(inputfile,"r") as infile:
    line = infile.readlines()

#print (line[0])
#print (line[1])

lineas_filtradas= [line for line in line if line.startswith('>')]

num_de_lineas= len(lineas_filtradas)

print(f"El archivo contiene {num_de_lineas} secuencias.")

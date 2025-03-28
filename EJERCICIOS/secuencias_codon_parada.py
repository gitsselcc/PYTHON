# Pedir al usuario que ingrese las secuencias de ADN separadas por comas
dna_input = input("Introduce las secuencias de ADN separadas por comas: ").split(',')

# Filtrar las secuencias que contienen un codón de parada
secuencias_codon_parada = [sequence for sequence in dna_input if 'TAA' in dna_input or 'TAG' in dna_input or 'TGA' in dna_input] 

# Imprimir las secuencias que contienen codones de parada
print("Las secuencias que contienen un codón de parada son:")
print(secuencias_codon_parada)


#Primero colocar un imput, asignandole a este una variable para manejarlo mas adelante.
#El input debe pedir las secuencias de DNA separadas por comas, antes de procesar esto, eliminamos las comas con split.
#Filtramos las secuencias que tienen codon de parada, primero le asiganmos una variable a nuestra lista, dentro hacemos el ciclo for, y ponemos la condicional.
#En la condicional tenemos un if (si 'codon de parada' esta en nuestro input) Lo hacemos con cada codon de parada

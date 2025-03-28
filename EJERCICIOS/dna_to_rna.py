# Pedir al usuario que ingrese las secuencias de ADN separadas por comas
dna_input = input("Introduce las secuencias de ADN separadas por comas: ").split(',')

# Dividir las secuencias ingresadas y convertir cada una de ADN a ARN
rna_sequences = [sequence.replace('T', 'U').replace('t', 'u') for sequence in dna_input]

# Imprimir las secuencias ya convertidas
print("Las secuencias de ARN son:")
print(rna_sequences)
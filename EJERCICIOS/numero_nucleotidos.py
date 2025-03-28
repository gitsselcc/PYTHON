# Pedir al usuario que ingrese varias secuencias de ADN separadas por comas
dna_input = input("Introduce las secuencias de ADN separadas por comas: ").upper().split(',')

# Dividir las secuencias y contar nucleótidos A, T, C, G para cada una
numero_nucleotidos = [
    [sequence.count('A'), sequence.count('T'), sequence.count('C'), sequence.count('G')]
    for sequence in dna_input
]

# Imprimir la lista con la cantidad de A, T, C, G para cada secuencia
print("Conteo de nucleótidos (A, T, C, G) para cada secuencia:")
print(numero_nucleotidos)
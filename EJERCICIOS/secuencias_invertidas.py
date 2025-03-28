# Pedir al usuario que ingrese las secuencias de ADN separadas por comas
dna_input = input("Introduce las secuencias de ADN separadas por comas: ").split(',')

# Dividir las secuencias y luego invertir cada una
reversed_sequences = [sequence[::-1] for sequence in dna_input]

# Imprimir las secuencias invertidas
print("Las secuencias invertidas son:")
print(reversed_sequences)
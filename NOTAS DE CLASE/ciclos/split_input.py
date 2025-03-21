#numeros_str = input("Dame tres numeros separados por espacio: ").split()
#print(map(int,numeros_str))

#print(numeros_str)
#suma= sum(numeros_str)
#print(suma)


numeros_str = input("Dame tres números separados por espacio: ").split()
numeros = list(map(int, numeros_str))  # Convertimos las cadenas a enteros

print(numeros)  # Imprime la lista de números como enteros
suma = sum(numeros)  # Calcula la suma de los números
print(f"La suma es: {numeros}")

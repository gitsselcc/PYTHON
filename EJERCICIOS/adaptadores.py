# Abrir el archivo de entrada y el archivo de salida
input_file= "4_input_adapters.txt"
output_file= "4_input_no_adapters.txt"
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        # Escribir la línea sin los primeros 14 caracteres, quitando los saltos de linea
        secuencia_limpia= line.strip()[14:] 
#Mandar esto a nuestro archivo de salida
        outfile.write(f"secuencia_limpia\n")

print("Proceso hecho, Las secuencias sin adaptadores están en '4_input_no_adapters.txt'.")
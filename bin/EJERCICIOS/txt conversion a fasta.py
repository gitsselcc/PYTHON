# Definir las rutas de los archivos, asignarle variables a cada uno
input_file = 'dna_sequences.txt'
output_file = 'dna_sequences.fa'

# Leer el archivo de entrada y escribir en el archivo de salida
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        # Dividir cada línea en ID de secuencia y la secuencia, separandolosos, quitando espacios.
        seq_id, sequence = line.strip().split('\t')
        # Escribir en formato FASTA
        outfile.write(f'>{seq_id}\n{sequence.upper()}\n')

print(f"Hemos Convertido a Formato Fasta. Las secuencias están guardadas en '{output_file}'.")
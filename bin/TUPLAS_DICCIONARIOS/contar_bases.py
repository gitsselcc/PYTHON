tupla_bases = tuple("ATGCTTCGA")
bases = ['A', 'T', 'G', 'C']
for base in bases:
    cantidad = tupla_bases.count(base)
    print(f"La base '{base}' esta {cantidad} veces")

sorteio = {1, 23}

print(f"Sorteio: {sorteio}")  # {1, 23}

copia_do_sorteio = sorteio.copy()

print(f"Sorteio: {sorteio}")  # {1, 23}
print(f"Cópia do Sorteio:{copia_do_sorteio}") # {1, 23}

copia_do_sorteio.add(2)
copia_do_sorteio.add(3)
print(f"Sorteio: {sorteio}")
print(f"Cópia do Sorteio: {copia_do_sorteio}")
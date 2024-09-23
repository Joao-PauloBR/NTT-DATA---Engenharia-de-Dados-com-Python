lista = [1, "Python", [40, 30, 20]]

copia_da_lista = lista.copy()

print(f"Essa é a lista: {lista}")  # [1, "Python", [40, 30, 20]]
print(f"Essa é a cópia da lista: {copia_da_lista}")

copia_da_lista.append("novo valor")
print(f"Essa é a cópia da lista com novo valor: {copia_da_lista}")
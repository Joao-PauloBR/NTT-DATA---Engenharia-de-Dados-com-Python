conjunto_a = {1, 2}
conjunto_b = {3, 4}

resultado = conjunto_a.union(conjunto_b)
print(resultado) # O resultado será a união dos conjuntos a e b = {1,2,3,4}

carros = {"Pálio", "Celta", "Gol", "Corsa", "Corolla"}
motocicleta = {"Yamaha", "Biz", "PcX"}
aeronave = {"avião GOL", "Jato", "Boeing"}
uniao = carros.union(motocicleta, aeronave)
print(uniao)
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.intersection(conjunto_b)
print(resultado)

carros = {"Pálio", "Celta", "Gol", "Corsa", "Corolla"}
motocicleta = {"Yamaha", "Biz", "PcX"}
aeronave = {"avião GOL", "Jato", "Boeing"}
intersecao = carros.intersection(motocicleta, aeronave)
print(intersecao) # set() significa um conjunto vazio, ou seja, não há interseção entre os dois conjuntos.
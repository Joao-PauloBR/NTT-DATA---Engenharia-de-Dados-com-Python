# O set utiliza as chaves. Para indicar que você está falando de conjuntos, precisa colocar as "{}"
# Suas particularidades são:
# - Permite que você coloque elementos repetidos, porém não irá mostrá-los
# - Não se pode acessar os elementos do conjunto diretamente pelo índice. É necessário transformá-los em lista ou utilizar um laço de repetição "for in enumerate"
# - Possui métodos matemáticos únicos, como ".union", ".intersection", etc. (lembre-se das operações entre conjuntos do Venn Euller) 

numeros = set([1, 2, 3, 1, 3, 4]) # Aqui, você está criando um conjunto a partir de uma lista. 
print(numeros)  # {1, 2, 3, 4}

letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"}

carros = set(("palio", "gol", "celta", "palio")) # Neste caso, você está criando um conjunto a partir de uma tupla.
print(carros)  # {"gol", "celta", "palio"}

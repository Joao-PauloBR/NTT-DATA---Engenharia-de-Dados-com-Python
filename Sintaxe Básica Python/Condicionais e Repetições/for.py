texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

# Utilizando função iterável
for letra in texto:
    if  letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()

# Utilizando a função built-in range
for numero in range(0, 11):
    print(numero, end=" ")

print() # só pra pular linha

# Tabuada do 5 utilizando a função built-in range
for numero in range(0,51,5):
    print(numero, end=" ")

print()
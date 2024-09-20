name = input(str("Digite o seu nome: "))
print(name)

age = input(str("Digite sua idade atual: "))

year = 2024 - int(age)

print(f"{name}, Você nasceu no ano {year}")

print(name, age, end="...\n")
print(name, age, sep="#", end="...\n")
print(name, age, sep="#")
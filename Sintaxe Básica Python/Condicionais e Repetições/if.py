MAIOR_IDADE = 18
MAXIMA_IDADE = 80

idade = int(input("Informe sua idade: "))

if idade >=MAIOR_IDADE and idade <= MAXIMA_IDADE:
    print("Você está apto para tirar sua CNH.")
elif idade < MAIOR_IDADE and idade >= 0:
    print("Você não possui idade suficiente.")
else:
    print("Que diabos é isso? Digita algum número real, caraio!")
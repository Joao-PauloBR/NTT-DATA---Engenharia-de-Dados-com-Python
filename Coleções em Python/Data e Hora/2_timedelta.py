# O timedelta é uma classe do módulo datetime que representa a diferença entre duas datas ou horários.
# É útil para fazer cálculos de tempo, como adicionar ou subtrair dias, horas, minutos e segundos de um objeto datetime.

from datetime import date, datetime, timedelta

tipo_carro = "M"  # P, M, G
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()
print(data_atual)

if tipo_carro == "P":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(days=tempo_medio)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
elif tipo_carro == "G":
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
else:
    print("Caracter inválido. Escolha entre M, P ou G.")

print(date.today() - timedelta(days=1))

resultado = datetime(2023, 7, 25, 10, 19, 20) - timedelta(hours=1)
print(resultado.time())

print(datetime.now().date())

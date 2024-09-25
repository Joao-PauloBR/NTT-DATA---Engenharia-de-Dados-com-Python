from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2023-10-20 10:20"
mascara_ptbr = "%d/%m/%Y %a %H:%M"
mascara_en = "%Y-%m-%d %H:%M"

print(data_hora_atual.strftime(mascara_ptbr))

data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(data_convertida)
print(type(data_convertida))

print("=" * 50)

data = []

data.append(datetime(2024, 7, 25, 15, 30))
data.append(datetime(2023, 6, 20, 10, 15))
mascara_ptbr = "%d/%m/%Y %a %H:%M"

for data in data:
    data_formatada = data
    print(data_formatada.strftime(mascara_ptbr))
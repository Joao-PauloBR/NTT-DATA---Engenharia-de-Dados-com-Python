# Ao importar apenas date, datetime e time, eu posso usar essas classes diretamente no meu código sem precisar referenciá-las
# como datetime.date, datetime.datetime e datetime.time. Isso torna o código mais limpo e fácil de ler.

from datetime import date, datetime, time

data = date(2011, 4, 25)
print(f"Data aleatória: {data}")
print(f"Data de HOJE: {date.today()}")

                       # DATA      # HORA
data_hora = datetime(2023, 7, 10, 18, 30, 50)
print(f"Data e hora aleatória: {data_hora}") # Ele deixa 00:00:00 caso eu não passe os valores de hora.
print(f"Data e hora de HOJE: {datetime.today()}")

hora = time(10, 20, 0)
print(f"Hora aleatória: {hora}")

# Caso eu queira exibir apenas o horário atual, uma vez que o .time() não possui um método .now()
resultado = datetime.now()
print(resultado.time())

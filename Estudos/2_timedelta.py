#trabalhando com timedelta

from datetime import datetime, timedelta, date

tipo_carro = "P"
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
date_atual = datetime.now()

if tipo_carro == 'P':
    data_estimada = date_atual + timedelta(minutes=tempo_pequeno)
    print(f'O carro chegou: {date_atual} e ficará entregue às {data_estimada}')
elif tipo_carro == "M":
    data_estimada = date_atual + timedelta(minutes=tempo_medio)
    print(f'O carro chegou: {date_atual} e ficará entregue às {data_estimada}')
else:
    data_estimada = date_atual + timedelta(minutes=tempo_grande)
    print(f'O carro chegou: {date_atual} e ficará entregue às {data_estimada}')
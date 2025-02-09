# trabalhando com formatação e conversão de datas 
# strftime e strptime

from datetime import datetime

dh_atual = datetime.now()
dh_str = "2023-10-20 10:20"
mascara_ptbr = "%d/%m/%Y %a"
mascara_en = "%Y-%m-%d %H:%M"

#A função strftime pode cortar os restantes do elemento de uma variavel (por exemplo as horas)
print(dh_atual.strftime(mascara_ptbr))

data_convertida = datetime.strptime(dh_str, mascara_en)
print(data_convertida)
print(type(data_convertida))
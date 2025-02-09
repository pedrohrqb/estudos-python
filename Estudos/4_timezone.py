#trabalhando com timezone
import pytz
from datetime import datetime, timezone, timedelta

#modelo de data com pytz
data = datetime.now(pytz.timezone("Europe/Oslo"))
data = datetime.now(pytz.timezone("America/Sao_Paulo"))

print(data)

#modelo de data com timezone

data_oslo = datetime.now(timezone(timedelta(hours=2)))
data_sao_paulo = datetime.now(timezone(timedelta(hours=-3)))

print(data_oslo)
print(data_sao_paulo)

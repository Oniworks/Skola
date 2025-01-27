import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=56.9496&longitude=24.1052&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m&timezone=auto&start_date=2025-01-24&end_date=2025-01-25"
items = requests.get(url)

# 1. Uzdevums
temps = list(items.json()["hourly"]["temperature_2m"])
moists = list(items.json()["hourly"]["relative_humidity_2m"])

# Aprēķina vidējo temperatūru ejot cauri visām vērtībām, pieskaitot tās summai un beigās dalot ar kopējo vērtību skaitu
temperatura = 0
for temp in temps:
    temperatura += temp
videja_temperatura = temperatura / len(temps)
print("Vidējā temperatūra ir ", videja_temperatura)

# Printē mazāko mitruma vērtību
print("Minimālais mitrums ir ", min(moists))

# 2. Uzdevums
laiks = list(items.json()["hourly"]["time"])
speeds = list(items.json()["hourly"]["wind_speed_10m"])

# Izveido sarakstus kuros ievietot vērtības, ja ātrums virs 20 km/h
s_over_20 = []
l_over_20 = []
t_over_20 = []
# Iet cauri vēja ātrumam un ja tas ir virs 20 km/h ievieto attiecīgo laiku, ātrumu un temperatūru izveidotajos sarakstos
for i in speeds:
    m = 0
    if i>20:
        s_over_20.append(i)
        t_over_20.append(temps[m])
        l_over_20.append(laiks[m])
        m += 1
# Izveido kopīgo sarakstu ar laikiem, ātrumiem un temperatūrām, kad ātrums virs 20 km/h
ir_virs_20 = list(zip(l_over_20, s_over_20, t_over_20))
print(ir_virs_20)

# 3. Uzdevums
print("Lielākais ātrums", max(speeds))

s_all = []
ti_all = []
te_all = []
m_all = []


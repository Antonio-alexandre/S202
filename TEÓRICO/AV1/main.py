import random
import threading
import time
from pymongo import MongoClient

# Conecta e cria o banco de dados
client = MongoClient('mongodb://localhost:27017')
db = client['bancoiot']
sensores = db['sensores']

sensores.update_many({}, {"$set": {"valorSensor": 0, "sensorAlarmado": False}}) # Inicializa os sensores com valores padrão

def randomTemp(sensor): # Função que gera temperaturas aleatórias
    while True:
        temperatura = random.randint(30,40)
        print(f"Sensor {sensor}: {temperatura} °C")

        sensores.update_one(
            {'nomeSensor': sensor},
            {'$set': {'valorSensor': temperatura}}
        )
        if temperatura > 38: # Se a temperatura for maior que 38 °C, o sensor é alarmado
            print(f"Temperatura muito alta no sensor: {sensor}!")
            sensores.update_one({"nomeSensor": sensor}, {"$set": {"sensorAlarmado": True}})
            break

        time.sleep(1)

sensors = ["Temp1", "Temp2", "Temp3"]
threads = []

for sensor in sensors: # Cria uma thread para cada sensor
    thread = threading.Thread(target=randomTemp, args=(sensor,))
    thread.start()
    threads.append(thread)

# Espera todas as threads terminarem
for thread in threads:
    thread.join()
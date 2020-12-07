






from machine import Pin
from time import sleep
import dht 
import machine
sensor = dht.DHT11(Pin(19))
while True:
  try:
    rtc = machine.RTC()
    hora = rtc.datetime()
    ano = hora[0]
    mes = hora[1]
    dia = hora[2]
    hrs = hora[4]
    min = hora[5]
    seg = hora[6]
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    arquivo = open("sensor_umidade.txt", "a")
    arquivo.write("id:"+str(hrs)+"   "+str(hum)+"  <-Valor"+" Data: "+str(dia)+"/"+str(mes)+"/"+str(ano)+" - "+str(hrs)+":"+str(min)+":"+str(seg) + "\n")
    arquivo.close()
    arquivo2 = open("sensor_temperatura.txt", "a")
    arquivo2.write("id:"+str(hrs)+"   "+str(temp)+"  <-Valor"+" Data: "+str(dia)+"/"+str(mes)+"/"+str(ano)+" - "+str(hrs)+":"+str(min)+":"+str(seg) + "\n")
    arquivo2.close()
    arquivo = open('tempo.txt', 'r')
    unica_string = arquivo.read()
    arquivo.close()
    sleep(60*int(unica_string))
  except OSError as e:
    print('Falha na leitura do sensor')

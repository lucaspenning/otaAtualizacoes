


import json
import ntptime
import os
import utime
import machine
from umqtt.simple import MQTTClient
from code_download import *
import _thread

#Variaveis
val_t = 0
val_u = 0
#Verifica se existe o arquivo de versionamento
try:
    f = open('src/.version')
    f.close()
    verifica = 1
except:
    verifica = 0
  
def sub_cb(topic, msg): 
  arquivo = open('comando.txt', 'w')
  arquivo.write(str(msg))
  arquivo.close()

#Configurar o Broker MQTT
mq = MQTTClient("AtualizacaoOTA","mqtt.dioty.co",1883,"lucas.penning@sou.ucpel.edu.br","ae8d0e1c")
mq.set_callback(sub_cb) 


#Led AMARELO(ATUALIZACOES)
pin17 = machine.Pin(17, machine.Pin.OUT)
#Led AMARELO(STATUS DA ATUALIZACAO)
pin18 = machine.Pin(18, machine.Pin.OUT)
pin18.value(1)

if(verifica == 1):
  f = open('src' + '/' + '.version')
  version = f.read()
  print(version)
  f.close()
  
def ver_atualizacao():
  #Virificando atualizacoes
  if(verifica == 1):
    if(version != version_v):
      os.chdir('/')
      print("Novas atualizacoes")
      horario_embarcado = rtc.datetime()
      ano_b = horario_embarcado[0]
      mes_b = horario_embarcado[1]
      dia_b = horario_embarcado[2]
      hrs_b = horario_embarcado[4]
      min_b = horario_embarcado[5]
      seg_b = horario_embarcado[6]
      arquivo_h = open("historico.txt", "a")
      arquivo_h.write("Nova Atualiza鑾借尗o: Vers鑼玱 "+str(version_v)+" Data: "+str(dia_b)+"/"+str(mes_b)+"/"+str(ano_b)+" - "+str(hrs_b)+":"+str(min_b)+":"+str(seg_b)+"\n")
      arquivo_h.close()
      #Conectando ao Broker MQTT e publicando 
      mq.connect()
      mq.publish(b"/lucas.penning@sou.ucpel.edu.br/",b"Sistema reiniciado, NOVO atualizacao, versao "+str(version_v))
      utime.sleep(1)
      #Rotina de piscagem do LED AMARELO
      pin17.value(1)
      utime.sleep_ms(1000)
      pin17.value(0)
      utime.sleep_ms(1000)
      pin17.value(1)
      utime.sleep_ms(1000)
      pin17.value(0)
    elif(version == version_v):
      print("Sem novas atualizacoes")
      #Conectando ao Broker MQTT e publicando
      mq.connect()
      mq.publish(b"/lucas.penning@sou.ucpel.edu.br/",b"Sistema reiniciado, SEM atualizar, versao "+str(version))
      utime.sleep(1)
      #Rotina de piscagem do LED AMARELO
      pin17.value(1)
      utime.sleep_ms(1000)
      pin17.value(0)  
  
#Baixando e Atualizando os codigos
def atualiza_ota():
  try:
      c = Code_download()
      c.download_update()
      pin18.value(0)
      _thread.start_new_thread(ver_atualizacao, ()) 
  except Exception as e:
      print('ERRO: ' +str(e)) 
  finally:
      os.chdir('/') #: usado para voltar para o diretorio / apos a execucao do codigo da pasta
  
atualiza_ota()  
  
if(verifica == 1):
  g = open('src' + '/' + '.version')
  version_v = g.read()
  print(version_v)
  g.close()
 

def escutando():  
  while True: 
    gc.collect()
    gc.mem_alloc()
    utime.sleep(2)
    arquivo = open('comando.txt', 'r')
    linha = arquivo.readline()
    comprimento = len(linha)
    palavra = linha[2:comprimento-1]
    print("Comando:" + palavra)
    mq.subscribe(topic="/lucas.penning@sou.ucpel.edu.br/")
    if(palavra != ''):
      arquivo = open('comando.txt', 'w')
      arquivo.write('')
      arquivo.close()
    if(palavra == 'version'):
      #Conectando ao Broker MQTT e publicando 
      mq.connect()
      mq.publish(b"/lucas.penning@sou.ucpel.edu.br/",b""+str(version_v))
      utime.sleep(1)
    if(palavra == 'reiniciar'):
      arquivo = open('comando.txt', 'w')
      arquivo.write('')
      arquivo.close()
      machine.reset()
      utime.sleep(1)
    if(palavra == 'horario'):
      rtc = machine.RTC()
      horario_embarcado = rtc.datetime()
      ano = horario_embarcado[0]
      mes = horario_embarcado[1]
      dia = horario_embarcado[2]
      hrs = horario_embarcado[4]
      min = horario_embarcado[5]
      seg = horario_embarcado[6]
      mq.connect()
      mq.publish(b"/lucas.penning@sou.ucpel.edu.br/",b""+str(dia)+"/"+str(mes)+"/"+str(ano)+" - "+str(hrs)+":"+str(min)+":"+str(seg))
      utime.sleep(1)
    if(palavra == 'uptime'):
      mq.connect()
      mq.publish(b"/lucas.penning@sou.ucpel.edu.br/",b""+str(dia_a)+"/"+str(mes_a)+"/"+str(ano_a)+" - "+str(hrs_a)+":"+str(min_a)+":"+str(seg_a))
      utime.sleep(1)
    if(palavra == 'atualizar'):
      mq.connect()
      mq.publish(b"/lucas.penning@sou.ucpel.edu.br/",b"Software atualizado")
      utime.sleep(1)
      atualiza_ota()
    if(palavra == 'sensores'):
      file = open('conf.json', 'r') #: le os dados do json
      file_json = ujson.loads(file.read())
      sensores = file_json['sensores']['tipo']
      mq.connect()
      mq.publish(b"/lucas.penning@sou.ucpel.edu.br/",b""+str(sensores))
      utime.sleep(1)
    if(palavra == 'temperatura'):
      val_t = 0
      content_variable = open('sensor_temperatura.txt ', "r")
      file_lines = content_variable.readlines()
      content_variable.close()
      last_line = file_lines[len(file_lines)-1]
      val_t = last_line[6:10]
      mq.connect()
      mq.publish(b"/lucas.penning@sou.ucpel.edu.br/",b""+str(val_t))
      utime.sleep(1)
    if(palavra == 'umidade'):
      val_u = 0
      content_variable = open('sensor_umidade.txt ', "r")
      file_lines = content_variable.readlines()
      content_variable.close()
      last_line = file_lines[len(file_lines)-1]
      val_u = last_line[6:10]
      mq.connect()
      mq.publish(b"/lucas.penning@sou.ucpel.edu.br/",b""+str(val_u))
      utime.sleep(1)
    if(palavra == 'logt'):  
      arquivo = open('sensor_temperatura.txt', 'r')
      unica_string = arquivo.read()
      arquivo.close()
      mq.connect()
      mq.publish(b"/lucas.penning@sou.ucpel.edu.br/",b""+str(unica_string))
      utime.sleep(1)
    if(palavra == 'logu'):  
      arquivo = open('sensor_umidade.txt', 'r')
      unica_string = arquivo.read()
      arquivo.close()
      mq.connect()
      mq.publish(b"/lucas.penning@sou.ucpel.edu.br/",b""+str(unica_string))
      utime.sleep(1)
    if(palavra == 'hist'):  
      arquivo = open('historico.txt', 'r')
      unica_string = arquivo.read()
      arquivo.close()
      mq.connect()
      mq.publish(b"/lucas.penning@sou.ucpel.edu.br/",b""+str(unica_string))
      utime.sleep(1)
    if(palavra == 'parametro'):  
      arquivo = open('tempo.txt', 'r')
      unica_string = arquivo.read()
      arquivo.close()
      if(int(unica_string) > 60):
        r = 10
      else:
        r = int(unica_string) + 10
      arquivo_h = open("tempo.txt", "w")
      arquivo_h.write(str(r))
      arquivo_h.close()
      mq.connect()
      mq.publish(b"/lucas.penning@sou.ucpel.edu.br/",b"Tempo de leitura:"+str(r))
      utime.sleep(1)
 
#Definindo Hor璋﹔io via NTP
def uptime():
  ntptime.settime()
  rtc = machine.RTC()
  utc_shift = -3
  tm = utime.localtime(utime.mktime(utime.localtime()) + utc_shift*3600)
  tm = tm[0:3] + (0,) + tm[3:6] + (0,)
  rtc.datetime(tm)
  
  
def rotina_verificacao():
  while True:
    rtc = machine.RTC()
    horario_embarcado = rtc.datetime()
    hrs = horario_embarcado[4]
    min = horario_embarcado[5]
    utime.sleep(30)
    if(hrs == 15 and min == 39):
      machine.reset()
  
def rotina_leitura():
  while True:
    rtc = machine.RTC()
    horario_embarcado = rtc.datetime()
    hrs = horario_embarcado[4]
    if hrs == 23:
      hrs = 0
    else:
      hrs += 1
  
    with open("sensor_umidade.txt", "r") as f:
      texto=f.readlines()
    with open("sensor_umidade.txt", "w") as f:
      for i in texto:
        if "id:"+str(hrs) not in i:
          f.write(i)
    
    with open("sensor_temperatura.txt", "r") as j:
      texto_a=j.readlines()
    with open("sensor_temperatura.txt", "w") as j:
      for i_a in texto_a:
        if "id:"+str(hrs) not in i_a:
          j.write(i_a)
    utime.sleep(1200)

#THREAD's
_thread.start_new_thread(uptime, ())
_thread.start_new_thread(rotina_leitura, ())
utime.sleep(1)
_thread.start_new_thread(rotina_verificacao, ())

utime.sleep(1)
_thread.start_new_thread(escutando, ())
utime.sleep(1)

#Ajustando hora
uptime()
rtc = machine.RTC()
horario_embarcado = rtc.datetime()
ano_a = horario_embarcado[0]
mes_a = horario_embarcado[1]
dia_a = horario_embarcado[2]
hrs_a = horario_embarcado[4]
min_a = horario_embarcado[5]
seg_a = horario_embarcado[6]

print("\n\nAgora vai comecar o codigo que foi baixado\n")
exec(open('src/exemplo.py').read()) #: como ja esta no diretorio que foi baixado os codigos executa o exemplo.py




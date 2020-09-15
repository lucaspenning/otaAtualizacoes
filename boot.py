
#

import os
import utime
import machine
from umqtt.simple import MQTTClient
from code_download import *
import _thread

#Verifica se existe o arquivo de versionamento
try:
    f = open('src/.version')
    f.close()
    verifica = 1
except:
    verifica = 0


#Configurar o Broker MQTT
mq = MQTTClient("AtualizacaoOTA","ioticos.org",1883,"G63VllTzA4939FY","46pnhP9OlrHX7vZ")


#Led VERDE(ATUALIZACOES)
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
      print("Novas atualizacoes")
      #Conectando ao Broker MQTT e publicando 
      mq.connect()
      mq.publish(b"oazafNBJA98GhyJ",b"Sistema reiniciado, NOVO atualizado, versao "+str(version_v))
      utime.sleep(1)
      #Rotina de piscagem do LED VERDE
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
      mq.publish(b"oazafNBJA98GhyJ",b"Sistema reiniciado, SEM atualizado, versao "+str(version))
      utime.sleep(1)
      #Rotina de piscagem do LED VERDE
      pin17.value(1)
      utime.sleep_ms(1000)
      pin17.value(0)  
  
#Baixando e Atualizando os codigos
try:
    c = Code_download()
    c.download_update()
    pin18.value(0)
    _thread.start_new_thread(ver_atualizacao, ()) 
except Exception as e:
    print('ERRO: ' +str(e)) 
finally:
    os.chdir('/') #: usado para voltar para o diretorio / apos a execucao do codigo da pasta
  
if(verifica == 1):
  g = open('src' + '/' + '.version')
  version_v = g.read()
  print(version_v)
  g.close()
 
def run():
      print("\n\nAgora vai comecar o codigo que foi baixado\n")
      exec(open('src/exemplo.py').read()) #: como ja esta no diretorio que foi baixado os codigos executa o exemplo.py
 
_thread.start_new_thread(run, ()) 

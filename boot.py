

#

#'''
import os
import utime
import machine
from umqtt.simple import MQTTClient
from code_download import *


mq = MQTTClient("AtualizacaoOTA","ioticos.org",1883,"G63VllTzA4939FY","46pnhP9OlrHX7vZ")

pin17 = machine.Pin(17, machine.Pin.OUT)
pin18 = machine.Pin(18, machine.Pin.OUT)
pin18.value(1)

f = open('src' + '/' + '.version')
version = f.read()
print(version)
f.close()

try:
    c = Code_download()
    c.download_update()
    print("\n\nAgora vai comecar o codigo que foi baixado\n")
    utime.sleep(2)
    exec(open('./exemplo.py').read()) #: como ja esta no diretorio que foi baixado os codigos executa o exemplo.py 
except Exception as e:
    print('ERRO: ' +str(e)) 
finally:
    os.chdir('/') #: usado para voltar para o diretorio / apos a execucao do codigo da pasta

g = open('src' + '/' + '.version')
version_v = g.read()
print(version_v)
g.close()


mq.connect()
mq.publish(b"oazafNBJA98GhyJ",b"Sistema Foi Reiniciado;")

if(version != version_v):
  print("Novas atualizações")
  pin18.value(0)
  mq.connect()
  mq.publish(b"oazafNBJA98GhyJ",b"Novas Atualizacoes;")
  mq.publish(b"oazafNBJA98GhyJ",b"Nova Versao: "+str(version_v))
  utime.sleep(1)
  pin17.value(1)
  utime.sleep_ms(1000)
  pin17.value(0)
  utime.sleep_ms(1000)
  pin17.value(1)
  utime.sleep_ms(1000)
  pin17.value(0)
elif(version == version_v):
  pin18.value(0)
  print("Sem novas atualizações")
  mq.connect()
  mq.publish(b"oazafNBJA98GhyJ",b"Sem Atualizacoes;")
  mq.publish(b"oazafNBJA98GhyJ",b"Versao Atual:"+str(version))
  utime.sleep(1)
  pin17.value(1)
  utime.sleep_ms(1000)
  pin17.value(0)
  
#'''

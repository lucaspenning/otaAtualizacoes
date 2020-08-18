
## Nome: Pisca_Thread.py
## Autor: Victor Hugo Lima
## Data: 13/05/2018
## Finalidade: Est茅 programa faz piscar dois leds em tempos diferentes atrav茅s de threads.

import _thread
import utime
import machine
pin21 = machine.Pin(21, machine.Pin.OUT)
pin19 = machine.Pin(19, machine.Pin.OUT)
 
def pisca1():
	while True:
		pin21.value(1)
		utime.sleep_ms(500)
		pin21.value(0)
		utime.sleep_ms(500)
def pisca2():
	while True:

		pin19.value(1)
		utime.sleep_ms(50)

		pin19.value(0)

		utime.sleep_ms(50)

_thread.start_new_thread(pisca1, ())

_thread.start_new_thread(pisca2, ())


import utime
import machine
pin21 = machine.Pin(19, machine.Pin.OUT)
pin19 = machine.Pin(21, machine.Pin.OUT)
pin21.value(1)
utime.sleep_ms(2500)
pin21.value(0)
utime.sleep_ms(500)
pin19.value(1)
utime.sleep_ms(2500)
pin19.value(0)
utime.sleep_ms(50)

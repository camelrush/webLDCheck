import requests
import pigpio
import time

LED_PIN = 4
CHECK_URL = 'http://localhost:3000/control/template2/'

pi = pigpio.pi()
pi.set_mode(LED_PIN ,pigpio.OUTPUT)
pin_val = 0

while(True):
    try:
        rq = requests.get(CHECK_URL)
        if rq.status_code == 200:
            pi.write(LED_PIN,1)
        else:
            pi.write(LED_PIN,0)
    except:
        pi.write(LED_PIN,0)
    time.sleep(1)



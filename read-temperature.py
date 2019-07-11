import os
import glob
import time
import threading
import requests

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
	temperature = {'tempC':temp_c}
        return temperature

def post():
	threading.Timer(1800.0, post).start()
	temperature = read_temp()
	data = temperature
	data['room'] = 'ROOM-NAME'
	print(data)

	url = 'POST-URL'
	query = data
	res = requests.post(url, data=query)
	print(res.text)

post()




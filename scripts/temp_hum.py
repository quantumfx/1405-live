import board
import adafruit_dht as dht
import datetime
import time

sensor = dht.DHT22(board.D4)
success = False
data_dir = '/home/pi/rpi_live/'
file_current = 'temp_humidity_current.csv'
file_history = 'temp_humidity.csv'

while success == False:
    try:
        temp = sensor.temperature
        humidity = sensor.humidity
    except RuntimeError as error:
        time.sleep(2.0)
        continue
    success = True

current_datetime = datetime.datetime.now().replace(microsecond=0).isoformat()

with open(data_dir+file_current, 'w') as f:
    f.write(current_datetime+','+str(temp)+','+str(humidity)+'\n')
with open(data_dir+file_history, 'a') as f:
    f.write(current_datetime+','+str(temp)+','+str(humidity)+'\n')

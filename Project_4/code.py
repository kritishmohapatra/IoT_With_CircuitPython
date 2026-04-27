import board
import adafruit_dht
import time

dht=adafruit_dht.DHT11(board.GP15)
while True:
    try:
        temp=dht.temperature
        hum=dht.humidity
        
        print(f" Temp is {temp:.1f} C | Humidity: {hum}%")
        
    except RuntimeError as error:
        print(f"Reading sensor: {error.args[0]}")
        time.sleep(2.0)
        continue
    except Exception as error:
        dht.device.exit()
        raise error
    time.sleep(2.0)
            

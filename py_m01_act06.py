''' IoT Greenhouse - Module 1: Activity 06
    Keith E. Kelly
    K2 Creatives, LLC
'''
from time import sleep
from iot_gh.IoTGreenhouseService import IoTGreenhouseService

ghs = IoTGreenhouseService()

l_readings = []
t_readings = []
print("Reading temperature and light levels.")
print("Press and hold push-button to end sampling.")
while ghs.switches.push_button.is_off():
    t_readings.append(ghs.temperature.get_outside_temp_F())
    l_readings.append(ghs.analog.light.get_value())
    print(".", end="")
    sleep(.5)
    
print()
print("temp", t_readings)
print()
print("light",l_readings)
print()

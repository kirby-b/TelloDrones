# This script turns on the motor meant to cool down the drone if it gets to hot
from djitellopy import tello
from time import sleep

drone = tello.Tello()

drone.connect()
# Connects to the drone

temp = drone.get_temperature()
if int(temp) >= 50:
    print("Temperature is too high turning on motor for cooling")
    drone.turn_motor_on()
    sleep(50)
    drone.turn_motor_off()
    sleep(5)
# turns on the fan motor without taking off to
# cool the drone if it gets to hot. Feel free to adjust
drone.end()

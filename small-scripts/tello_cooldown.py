from djitellopy import tello
from time import sleep

drone = tello.Tello()

drone.connect()
sleep(1)
# connects
drone.turn_motor_on()
sleep(30)
drone.turn_motor_off()
# Turns the cooling motor on for 30 seconds

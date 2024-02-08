from djitellopy import tello
from time import sleep

drone = tello.Tello()

drone.connect()
sleep(1)
drone.initiate_throw_takeoff() 
sleep(5)
# connects and takes off
drone.flip("b")
drone.land()
# lands
drone.turn_motor_on()
sleep(10)
drone.turn_motor_off()
# Turns the cooling motor on for 10 seconds

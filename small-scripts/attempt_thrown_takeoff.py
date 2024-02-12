from djitellopy import tello
from time import sleep

drone = tello.Tello()

drone.connect()
sleep(1)
drone.initiate_throw_takeoff() 
sleep(5)
# connects and attempts thrown take off
drone.flip("b")
drone.land()
# flips and lands
drone.turn_motor_on()
sleep(10)
drone.turn_motor_off()
# Turns the cooling motor on for 10 seconds

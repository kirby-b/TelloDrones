from djitellopy import tello
from time import sleep

drone = tello.Tello()

drone.connect()
sleep(1)
# connects
drone.query_battery()
# gets the battery percent
sleep(1)
drone.takeoff()
sleep(4)
# takes off
drone.flip("l")
sleep(9)
drone.flip("r")
sleep(9)
drone.flip("f")
sleep(9)
drone.flip("b")
sleep(9)
# flips the drone left, right, backward, then forward
drone.land()
# lands
drone.turn_motor_on()
sleep(10)
drone.turn_motor_off()
# Turns the cooling motor on for 10 seconds

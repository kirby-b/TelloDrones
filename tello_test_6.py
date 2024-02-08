from djitellopy import tello
from time import sleep

drone = tello.Tello()

drone.connect()
sleep(1)
drone.takeoff()
sleep(4)
# connects and takes off
for i in range(3):
    drone.flip("l")
    sleep(8)
    drone.rotate_clockwise(360)
    sleep(8)
    drone.flip("r")
    sleep(8)
# flips left, rotates all the way around, flips back 3 times
drone.land()
# lands
drone.turn_motor_on()
sleep(10)
drone.turn_motor_off()
# Turns the cooling motor on for 10 seconds

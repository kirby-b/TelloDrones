# This script is test from moving up and down
from djitellopy import tello
from time import sleep

drone = tello.Tello()

drone.connect()
sleep(1)
# connects and sleeps to ensure it is ready
sleep(1)
drone.takeoff()
sleep(4)
# takes off
drone.move_up(60)
sleep(7)
drone.move_down(60)
sleep(7)
# moves up then down
drone.land()
# lands
drone.end()

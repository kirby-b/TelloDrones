# This script tries to initiate a thrown takeoff
from djitellopy import tello
from time import sleep

drone = tello.Tello()

drone.connect()
sleep(1)
drone.initiate_throw_takeoff() 
sleep(5)
# connects and attempts thrown take off.
# This is iffy and I rarely get the drone to recognize it had been thrown
drone.flip("b")
drone.land()
# flips and lands
drone.end()

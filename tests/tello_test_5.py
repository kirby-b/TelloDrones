# This script is a sort of stress test to check looping and making sure the drone can go for a while
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

# I decided to make the two movements be in loops
# so this isnt as long and to keep best practice

for i in range(5):
    drone.flip("l")
    sleep(6)
    drone.rotate_clockwise(360)
    sleep(7)
# flips the drone left and does a 360 clockwise 5 times
# It sleeps in between each so the drone doesnt error
for i in range(5):
    drone.flip("r")
    sleep(6)
    drone.rotate_counter_clockwise(360)
    sleep(7)
# flips the drone left and does a 360 counter-clockwise 5 times
# It sleeps in between each so the drone doesnt error
drone.land()
# lands
drone.end()

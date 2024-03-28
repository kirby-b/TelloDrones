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
for i in range(5):
    drone.flip("l")
    sleep(6)
    drone.rotate_clockwise(360)
    sleep(7)
# flips the drone left and does a 360 clockwise 5 times
for i in range(5):
    drone.flip("r")
    sleep(6)
    drone.rotate_counter_clockwise(360)
    sleep(7)
# flips the drone left and does a 360 counter-clockwise 5 times
drone.land()
# lands
drone.end()

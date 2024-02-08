from djitellopy import tello
from time import sleep

drone = tello.Tello()

drone.connect()
sleep(1)
drone.takeoff()
sleep(4)
# connects and takes off
drone.rotate_counter_clockwise(90)
sleep(8)
drone.rotate_clockwise(90)
sleep(8)
# rotates back and forth
drone.land()
# lands

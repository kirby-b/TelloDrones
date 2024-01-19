from djitellopy import tello
from time import sleep

drone = tello.Tello()

drone.connect()
drone.takeoff()
sleep(3)
# connects and takes off
drone.rotate_counter_clockwise(90)
sleep(5)
drone.rotate_clockwise(90)
sleep(5)
# rotates back and forth
drone.land()
# lands

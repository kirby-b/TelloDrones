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
# Takes off
drone.rotate_counter_clockwise(90)
sleep(10)
drone.rotate_clockwise(90)
sleep(10)
# rotates back and forth
drone.land()
# lands

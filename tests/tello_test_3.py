#This is a long distance test
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
# connects and takes off
drone.move_forward(400)
sleep(6)
drone.rotate_clockwise(180)
sleep(5)
drone.move_forward(400)
sleep(6)
drone.rotate_clockwise(180)
sleep(5)
# moves forward
drone.land()
# lands
drone.end()
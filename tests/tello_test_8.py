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
drone.move_up(60)
sleep(10)
drone.move_down(60)
sleep(10)
# Moves up and down
drone.rotate_counter_clockwise(90)
sleep(10)
drone.rotate_clockwise(90)
sleep(10)
# Rotates back and forth
drone.move_forward(100)
sleep(10)
drone.move_back(100)
sleep(10)
drone.move_left(100)
sleep(10)
drone.move_right(100)
sleep(10)
# Moves back, forward, left, right
drone.rotate_clockwise(360)
sleep(10)
drone.rotate_counter_clockwise(360)
sleep(10)
# Rotates 360 in both directions
drone.land()
# lands

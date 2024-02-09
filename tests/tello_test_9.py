# This will be the same as 7 but I set the speed higher
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
drone.set_speed(50)
sleep(10)
drone.move_up(50)
sleep(10)
drone.move_forward(100)
sleep(10)
drone.move_down(50)
sleep(10)
drone.move_back(100)
sleep(10)
drone.rotate_clockwise(360)
# moves up, down, and rotates 360
drone.land()
# lands
drone.turn_motor_on()
sleep(15)
drone.turn_motor_off()
# Turns the cooling motor on for 15 seconds
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
drone.move_forward(100)
sleep(5)
# moves forward
drone.land()
# lands
drone.turn_motor_on()
sleep(10)
drone.turn_motor_off()
# Turns the cooling motor on for 10 seconds

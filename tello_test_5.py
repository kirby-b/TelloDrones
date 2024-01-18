from djitellopy import tello
from time import sleep

drone = tello.Tello()

drone.connect()
# Connects to the drone

drone.query_battery()
# gets the battery percent

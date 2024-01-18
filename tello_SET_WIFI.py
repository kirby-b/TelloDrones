from djitellopy import tello
from time import sleep

drone = tello.Tello()

drone.connect()
# Connects to the drone

drone.set_wifi_credentials('TelloDrone1!', 'Password123!')
# sets the wifi ssid and password. Definately change these to your own.

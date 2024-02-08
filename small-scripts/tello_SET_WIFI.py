from djitellopy import tello

drone = tello.Tello()

drone.connect()
# Connects to the drone

drone.set_wifi_credentials('TelloDrone1!', 'Password123!')
# sets the wifi ssid and password. Definately change these to your own.

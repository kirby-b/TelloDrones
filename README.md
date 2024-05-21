# Tello Drones

## Sections
[Installing/Using](#installing-and-using)

[Uses](#uses-for-these-scripts)

[Bugs](#bugs-i-have-encountered)

[Links](#links)

## Installing and using
Programming DJI Tello Drones. Make sure to install the dji tello library before using these.

To install the dji tello library just run: **pip install djitellopy** in your command line. You may need to run the command line as admin

To run you will need a computer that can connect to wifi. Ethernet only computers cannot connect to drones as far as I'm aware.

You will also need packet sender to use UDP and connect to the drone in sdk mode. In packet sender you need to make the packet: name "command" and ASCII of "command". Do not send the "command" command in packet sender, if you do the code will error and nothing will happen. The code itself runs the "command" command when you run it, but you should be able to stop that by deleting the drone.connect() line.

You can also make an ap command to connect your drone to your wifi with: name "ap" and ASCII of "ap ROUTER_SSID ROUTER_PASSWORD" . This makes it easy to create a drone swarm

Make sure both packets as under IP 192.168.10.1 ,  port 8889 , and type UDP

## Uses for these scripts
These scripts are not very complicated and are very basic at their core, But they can still be a fun way to learn how Tello Drones work. Considering the original idea was for testing tellos, they are nice for benchmarking and testing tellos too.

If you are a teacher who somehow found this repo, please feel free to use it. 

## Bugs I have encountered

All solutions for bugs I know of can be found here or in the below links

1. Problem: Drone keeps erroring and saying it doesnt recognize commands
* Solution: This is usyally because the drone is to hot or the firmware needs updated. The update can be done in the [dji tello app](https://www.dji.com/downloads/djiapp/tello)
2. Problem: The successfully does some commands and the fails/errors.
* Solution: Some of the drone commands are based on the camera on the drone and they need light to be done, so make sure you are in a well lit area. Another possible solution is to add more time between commands as sometimes the drones will end up running multiple commands at once. Lastly, the things mentioned in the solution for problem 1 have a possibility of working
3. Problem: The drone flips to one side when it takes off
* Solution: One of the sides has blades flipped and you should just switch them around.
  
Another thing that likes to randomly work in terms of bug fixing is just doing a soft reset by long pressing the power button, or even just turning it off and on again.

## Links

https://djitellopy.readthedocs.io/en/latest/tello/

https://github.com/damiafuentes/DJITelloPy

https://pypi.org/project/djitellopy/

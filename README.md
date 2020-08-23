# home-automation-based-on-raspberry-pi-and-adafruit-io-
- original code :https://github.com/adafruit/Adafruit_IO_Python
- from this python code you can control 2 led ,a servo motor and sending a random value into adafruit io cloud which represent a temperature and humidity
- the servo motor turns automatically into right when the led 1 turns on and the indicator switch into green color in the dashboard indicates that the door opened
- when the led 1 turned off the servo motor turns automatically into left and the color of indicator become red

![](IMG_20200822_135441_2.jpg)

# The imoprtant steps
1 Create an account in io.adafruit.com
2 Create the feeds(Door,humidity,temperature,room1,rrom2)
3 Create a dashboard
4 Add the blocks into dashborad(gauge,line chart,togle,indicator)
5 Install the important adafruit library into raspberry pi (pip3 install adafruit-io)
6 Connect the components (led,servo motor) into GPIO of raspberry pi
7 Download the code from the link and update you username and active key


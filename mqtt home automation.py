# Import standard python modules.
import random
import sys
import RPi.GPIO as GPIO
import time
from Adafruit_IO import MQTTClient

GPIO.setmode(GPIO.BCM) 

def Door_control(x,pin):
       
       GPIO.setup(pin,GPIO.OUT)
       GPIO.output(pin,1)
       servo=GPIO.PWM(pin,50)
       servo.start(12.5)
       servo.ChangeDutyCycle(x)
       time.sleep(0.6)
       GPIO.output(pin,0)
       if x==2.5  :
         print("door open")        
       else :
         print("door close")
        
def light(pin,status):
 GPIO.setup(pin,GPIO.OUT)
 if(status=='ON'):
  GPIO.output(pin,1)
 else:
  GPIO.output(pin,0)
 

def random_val(min_val,max_val):
 return random.randint(min_val,max_val)

# Set to your Adafruit IO key.
ADAFRUIT_IO_KEY = 'your active key'
# Set to your Adafruit IO username.
ADAFRUIT_IO_USERNAME = 'you name'

def connected(client):
    print('Connected to Adafruit IO!  Listening for changes...')
    # Subscribe to changes on a feed .
    client.subscribe('room1')
    client.subscribe('room2')

def disconnected(client):
    # Disconnected function will be called when the client disconnects.
    print('Disconnected from Adafruit IO!')
    sys.exit(1)

def message(client, feed_id, payload):
    # Message function will be called when a subscribed feed has a new value.
    # The feed_id parameter identifies the feed, and the payload parameter has
    # the new value.
    print('Feed {0} received new value: {1}'.format(feed_id, payload))
    if(feed_id=='room1'):
     print("Room 1 is turned ",payload)
     light(26,payload)
     if(payload=='ON'):
      Door_control(2.5,13)
      client.publish('Door', '1')
     else:
      Door_control(7.5,13)
      client.publish('Door', '0')
    if(feed_id=='room2'):
     print("Room 2 is turned ",payload)
     light(19,payload)
    
# Create an MQTT client instance.
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
# Setup the callback functions defined above.
client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message
# Connect to the Adafruit IO server.
client.connect()
# Now the program needs to use a client loop function to ensure messages are
# sent and received.  There are a few options for driving the message loop,
# depending on what your program needs to do.

# The first option is to run a thread in the background so you can continue
# doing things in your program.
client.loop_background()
# Now send new values every 10 seconds.
interval=10
print('Publishing a new message every ' , interval,'seconds (press Ctrl-C to quit)...')
while True:
    temp = random_val(0,50)
    print(' temperature value {0} {1}'.format(temp,"C °"))
    client.publish('temperature', temp)
    hum = random_val(7,100)
    print(' humidity value {0} {1}'.format(hum,"%"))
    client.publish('humidity', hum)
    time.sleep(interval)



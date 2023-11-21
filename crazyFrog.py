import RPi.GPIO as GPIO
from time import sleep

buzzPin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzPin, GPIO.OUT)
buzz = GPIO.PWM(buzzPin, 349.23)

f = 349.23

quarter = .5
eighth = .25
sixteenth = .125

def measure1():
        # F
        buzz.start(50)
        buzz.ChangeFrequency(f)
        sleep(quarter/2)
        buzz.stop()
        sleep(quarter/2)
        #buzz.start(50)
        # Ab
        buzz.ChangeFrequency(f*(6/5))
        buzz.start(50)
        sleep(eighth+(sixteenth/2))
        buzz.stop()
        sleep(sixteenth/2)
        # F
        buzz.ChangeFrequency(f)
        buzz.start(50)
        sleep(eighth/2)
        buzz.stop()
        sleep(eighth/2)
        # F
        buzz.ChangeFrequency(f)
        buzz.start(50)
        sleep(sixteenth/2)
        buzz.stop()
        sleep(sixteenth/2)
        # Bb
        buzz.ChangeFrequency(f*(4/3))
        buzz.start(50)
        sleep(sixteenth*.75)
        buzz.stop()
        sleep(sixteenth*.25)
        # F
        buzz.ChangeFrequency(f)
        sleep(eighth/2)
        buzz.start(50)
        sleep(eighth/2)
        buzz.stop()
        sleep(eighth/2)
        # Eb
        buzz.ChangeFrequency(f*(8/9))
        buzz.start(50)
        sleep(eighth/2)
        buzz.stop()
        sleep(eighth/2)

def measure2():
      # F
        buzz.start(50)
        buzz.ChangeFrequency(f)
        sleep(quarter/2)
        buzz.stop()
        sleep(quarter/2)
        #buzz.start(50)
        # C
        buzz.ChangeFrequency(f*(3/2))
        buzz.start(50)
        sleep(eighth+(sixteenth/2))
        buzz.stop()
        sleep(sixteenth/2)
        # F
        buzz.ChangeFrequency(f)
        buzz.start(50)
        sleep(eighth/2)
        buzz.stop()
        sleep(eighth/2)
        # F
        buzz.ChangeFrequency(f)
        buzz.start(50)
        sleep(sixteenth/2)
        buzz.stop()
        sleep(sixteenth/2)
        # D
        buzz.ChangeFrequency(f*(5/3))
        buzz.start(50)
        sleep(sixteenth*.75)
        buzz.stop()
        sleep(sixteenth*.25)
        # C
        buzz.ChangeFrequency(f*(3/2))
        sleep(eighth/2)
        buzz.start(50)
        sleep(eighth/2)
        buzz.stop()
        sleep(eighth/2)
        # Ab
        buzz.ChangeFrequency(f*(6/5))
        buzz.start(50)
        sleep(eighth/2)
        buzz.stop()
        sleep(eighth/2)

def measure3():
       # F
        buzz.start(50)
        buzz.ChangeFrequency(f)
        sleep(eighth/2)
        buzz.stop()
        sleep(eighth/2)
        #buzz.start(50)
        # C
        buzz.ChangeFrequency(f*(3/2))
        buzz.start(50)
        sleep(eighth/2)
        buzz.stop()
        sleep(eighth/2)
        # F
        buzz.ChangeFrequency(f*2)
        buzz.start(50)
        sleep(eighth/2)
        buzz.stop()
        sleep(eighth/2)
        # F
        buzz.ChangeFrequency(f)
        buzz.start(50)
        sleep(sixteenth/2)
        buzz.stop()
        sleep(sixteenth/2)
        # Eb
        buzz.ChangeFrequency(f*(8/9))
        buzz.start(50)
        sleep(eighth/2)
        buzz.stop()
        sleep(eighth/2)
        # Eb
        buzz.ChangeFrequency(f*(8/9))
        buzz.start(50)
        sleep(sixteenth/2)
        buzz.stop()
        sleep(sixteenth/2)
        # Middle C
        buzz.ChangeFrequency(f*(2/3))
        buzz.start(50)
        sleep(eighth/2)
        buzz.stop()
        sleep(eighth/2)
        # G
        buzz.ChangeFrequency(f*(9/8))
        buzz.start(50)
        sleep(eighth/2)
        buzz.stop()
        sleep(eighth/2)
        # F
        buzz.ChangeFrequency(f)
        buzz.start(50)
        sleep(quarter/2)
        buzz.stop()
        sleep(quarter/2)
        sleep(1)
        # F
        buzz.ChangeFrequency(f*2)
        buzz.start(50)
        sleep(quarter/2)
        buzz.stop()
        sleep(quarter/2)
        # F
        buzz.ChangeFrequency(f*2)
        buzz.start(50)
        sleep(quarter/2)
        buzz.stop()
        sleep(quarter/2)


try:
    while True:
        measure1()
        measure2()
        measure3()
        



except KeyboardInterrupt:
    GPIO.cleanup()
    print('\nadios')

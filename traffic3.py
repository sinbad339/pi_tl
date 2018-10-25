3#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      johnd
#
# Created:     30/07/2018
# Copyright:   (c) johnd 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import RPi.GPIO as GPIO
import time

def measure_dist():

	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)

	while GPIO.input(ECHO) == False:
		start = time.time()

	while GPIO.input(ECHO) == True:
		end = time.time()

	sig_time = end-start

	#CM:
	#distance = sig_time / 0.000058

	#inches:
	distance = sig_time / 0.000148
	
	return(distance)

if __name__ == '__main__':

    GPIO.setmode(GPIO.BCM)

    TRIG = 4
    ECHO = 18

    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)

    while True:
		my_dist = measure_dist()
		print('Distance: {} inches'.format(my_dist))

		print ' '
		time.sleep(1.0)
##        [red, green, yellow] = SundayAtTheSpeedway()
##        print 'Red is ', red
##        print 'Yellow is ', yellow
##        print 'Green is ', green
##        print '======================='
##
##        time.sleep(1)


    GPIO.cleanup()

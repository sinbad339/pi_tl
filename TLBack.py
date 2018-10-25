#-------------------------------------------------------------------------------
# Name:        TLBack
# Purpose:
#
# Author:      jdilorenzo
#
# Created:     12/09/2018
# Copyright:   (c) jdilorenzo 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from Queue import Queue
import csv
import time
import copy
import random
from copy import deepcopy
import RPi.GPIO as GPIO

def get_base():
    csvfile = open('/home/pi/Documents/Flask/tl_cfg.csv', 'r')
    readCSV = csv.reader(csvfile, delimiter=',')
    csvfile.close

    cfg_tuple = []

    for row in readCSV:
        cfg_tuple.append(row)

    return(cfg_tuple)

def save_base(entries):

    res_f = open('/home/pi/Documents/Flask/tl_cfg.csv', "wb")
    writer = csv.writer(res_f)
    writer.writerows(entries)
    res_f.close()

    return()

def run_amok(q):

    GPIO.setmode(GPIO.BCM)

    TRIG = 4
    ECHO = 3
    
    RedDrv = 17
    YelDrv = 27
    GrnDrv = 22

    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    
    GPIO.setup(RedDrv,GPIO.OUT)
    GPIO.setup(YelDrv,GPIO.OUT)
    GPIO.setup(GrnDrv,GPIO.OUT)

    old_mode = "junk"

    this_cfg = q.get()

    while True:

        mode = this_cfg[0][1]
        tl_rate = float(this_cfg[1][1])
        grn_ylo_dist = float(this_cfg[2][1])
        ylo_red_dist = float(this_cfg[3][1])
        hysterysis = float(this_cfg[4][1])
        speed_rate = float(this_cfg[5][1])
        force_red = this_cfg[6][1]
        force_ylo = this_cfg[7][1]
        force_grn = this_cfg[8][1]

        green_on_time = 50 / tl_rate
        yellow_on_time = 10 / tl_rate
        red_on_time = 50 / tl_rate

# detect mode change
        if mode != old_mode:
            # Initialze the Traffic Light mode
            red_state = 0
            yellow_state = 0
            green_state= 1
            green2yellow_time = time.time() + green_on_time
            start = time.time()

            old_mode = deepcopy(mode)
            print "I'm doing ", mode
            
            filt_dist = 0.0

        if mode == "Traffic Light":
            if green_state == 1:
                if time.time() > green2yellow_time:
                    green_state = 0
                    yellow_state = 1
                    yellow2red_time = time.time() + yellow_on_time
#                    print "It's Yellow"

            if yellow_state == 1:
                if time.time() > yellow2red_time:
                    yellow_state= 0
                    red_state= 1
                    red2green_time = time.time() + red_on_time
#                    print "It's Red"

            if red_state == 1:
                if time.time() > red2green_time:
                    red_state= 0
                    green_state= 1
                    green2yellow_time = time.time() + green_on_time
#                    print "It's Green"

        elif mode == "Parking Distance":
#            print "I'm doing Parking Distance"

            GPIO.output(TRIG, True)
            time.sleep(0.00001)
            GPIO.output(TRIG, False)

            while GPIO.input(ECHO) == False:
                start = time.time()

            while GPIO.input(ECHO) == True:
                end = time.time()

            sig_time = end-start

            distance = sig_time / 0.000148
            print('Distance: {} inches'.format(distance))

            if green_state == 1:
                if distance < grn_ylo_dist:
#	    			print "The light is yellow"
	    			red_state = 0
	    			yellow_state = 1
	    			green_state = 0

            if yellow_state == 1:
                if distance > grn_ylo_dist + hysterysis:
#	    			print "The light is green"
	    			red_state = 0
	    			yellow_state = 0
	    			green_state = 1

                elif distance < ylo_red_dist - hysterysis:
#	    			print "The light is red"
	    			red_state = 1
	    			yellow_state = 0
	    			green_state = 0

            if red_state == 1:
                if distance > ylo_red_dist:
#	    			print "The light is yellow"
	    			red_state = 0
	    			yellow_state = 1
	    			green_state = 0

            if abs(distance - filt_dist) < 3.0:
				red_state = 0
				yellow_state = 0
				green_state = 0

            filt_dist = filt_dist * (1 - 1/240.0) + distance/240.0
            print('Filtered Distance: {} inches'.format(filt_dist))
            time.sleep(0.5)

        elif mode == "Sunday at the Speedway":
#            print "I'm doing Sunday at the Speedway"
            x = random.uniform(0.0, 1.0)
            if x < 0.5:
                red_state = 0
            else:
                red_state = 1
            x = random.uniform(0.0, 1.0)
            if x < 0.5:
                yellow_state = 0
            else:
                yellow_state = 1
            x = random.uniform(0.0, 1.0)
            if x < 0.5:
                green_state = 0
            else:
                green_state = 1

#            print "red, yellow, green = ", red_state, yellow_state, green_state
            time.sleep(30/speed_rate)

        elif mode == "Force":
#            print "I'm doing Force"
            red_state = 0
            yellow_state = 0
            green_state = 0

            if force_red == 1:
				red_state = 1
            if force_ylo == 1:
				yellow_state = 1
            if force_grn == 1:
				green_state = 1

        else:
            print "I don't know this mode"
            time.sleep(1)

        if not q.empty():
            this_cfg = q.get()
            print "\n\n\nGot a new configuration\n\n\n"

        if red_state == 1:
            GPIO.output(RedDrv, True)
        else:
			GPIO.output(RedDrv, False)

        if yellow_state == 1:
            GPIO.output(YelDrv, True)
        else:
			GPIO.output(YelDrv, False)

        if green_state == 1:
            GPIO.output(GrnDrv, True)
        else:
			GPIO.output(GrnDrv, False)

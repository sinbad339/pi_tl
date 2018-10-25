#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      johnd
#
# Created:     03/08/2018
# Copyright:   (c) johnd 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys
import csv
import time
import copy
from copy import deepcopy

def save_cfg(entries):

    res_f = open('tl_cfg.csv', "wb")
    writer = csv.writer(res_f)
    writer.writerows(entries)
    res_f.close()

    return()

def load_cfg():

    rd_tuple = []

    with open('tl_cfg.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            rd_tuple.append((row[0], row[1]))
##         row = next(reader)

    return rd_tuple

if __name__ == '__main__':

    old_mode = "junk"
    
    while True:

        this_cfg = load_cfg()

        mode = this_cfg[0][1]
        tl_rate = float(this_cfg[1][1])
        grn_ylo_dist = float(this_cfg[2][1])
        ylo_red_dist = float(this_cfg[3][1])
        hysterysis = float(this_cfg[4][1])
        speed_rate = float(this_cfg[5][1])
        force_red = this_cfg[6][1]
        force_ylo = this_cfg[7][1]
        force_grn = this_cfg[8][1]

        green_on_time = 30 * tl_rate
        yellow_on_time = 5 * tl_rate
        red_on_time = 30 * tl_rate

# detect mode change
        if mode != old_mode:
            # Initialze the Traffic Light mode
            red_state = 0
            yellow_state = 0
            green_state= 1
            green2yellow_time = time.time() + green_on_time

            old_mode = deepcopy(mode)
            print "I'm doing ", mode

        if mode == "Traffic Light":
            if green_state == 1:
                if time.time() > green2yellow_time:
                    green_state = 0
                    yellow_state = 1
                    yellow2red_time = time.time() + yellow_on_time

            if yellow_state == 1:
                if time.time() > yellow2red_time:
                    yellow_state= 0
                    red_state= 1
                    red2green_time = time.time() + red_on_time

            if red_state == 1:
                if time.time() > red2green_time:
                    red_state= 0
                    green_state= 1
                    green2yellow_time = time.time() + green_on_time
        print "Green: ", green_state, " Yellow: ", yellow_state, " Red: ", red_state

        if mode == "Parking Distance":
            print "I'm doing Parking Distance"

        if mode == "Sunday at the Speedway":
            print "I'm doing Sunday at the Speedway"

        if mode == "Force":
            print "I'm doing Force"


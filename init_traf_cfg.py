#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      johnd
#
# Created:     02/08/2018
# Copyright:   (c) johnd 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys
import csv

def save_base(entries):

    res_f = open('tl_cfg.csv', "wb")
    writer = csv.writer(res_f)
    writer.writerows(entries)
    res_f.close()

    return()

def main():
    pass

if __name__ == '__main__':

    wr_tuple = []

    field = "Mode"
    value = "Traffic Light"
    wr_tuple.append((field, value))

    field = "TL Distance"
    value = 0.5
    wr_tuple.append((field, value))

    field = "GreenYellowDist"
    value = 24
    wr_tuple.append((field, value))

    field = "YellowRedDist"
    value = 5
    wr_tuple.append((field, value))

    field = "histersis"
    value = 1
    wr_tuple.append((field, value))

    field = "SpeedRate"
    value = .5
    wr_tuple.append((field, value))

    field = "ForceRed"
    value = 0
    wr_tuple.append((field, value))

    field = "ForceYellow"
    value = 0
    wr_tuple.append((field, value))

    field = "ForceGreen"
    value = 0
    wr_tuple.append((field, value))

    save_base(wr_tuple)

    print "Done"
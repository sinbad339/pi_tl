#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      johnd
#
# Created:     08/09/2018
# Copyright:   (c) johnd 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from flask import Flask, request, render_template
import csv

global rd_tuple

app = Flask(__name__)

@app.route('/')
def my_form():
    print 'This is the root url call'
    if request.method == 'GET':
        my_form.tl_rate.data = 0.111
        my_form.g2y_dist.data = 0.222

    return render_template('my-form.html')

@app.route('/', methods=['GET', 'POST'])
def my_form_post():
    print 'This is the methods call'
    text = request.form['text']
    processed_text = text.upper()
    return processed_text

if __name__ == "__main__":

    csvfile = open('tl_cfg.csv', 'r')
    readCSV = csv.reader(csvfile, delimiter=',')
    rd_tuple = []

    for row in readCSV:
        rd_tuple.append(row)

    mode = rd_tuple[0][1]
    tl_distance = rd_tuple[1][1]
    GreenYellowDist = rd_tuple[2][1]
    YellowRedDist = rd_tuple[3][1]
    histersis = rd_tuple[4][1]
    SpeedRate = rd_tuple[5][1]
    ForceRed = rd_tuple[6][1]
    ForceYellow = rd_tuple[7][1]
    ForceGreen = rd_tuple[8][1]

#   app.run(host='0.0.0.0', port=80, debug=True)
    app.run(host='0.0.0.0', port=80, debug=True)

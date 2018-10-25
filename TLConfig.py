#-------------------------------------------------------------------------------
# Name:        TLConfig
# Purpose:
#
# Author:      jdilorenzo
#
# Created:     11/09/2018
# Copyright:   (c) jdilorenzo 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from flask import Flask, render_template, request, flash
from forms import ConfigureForm
import threading
from Queue import Queue
import csv

from TLBack import *

app = Flask(__name__)
app.secret_key = '1930FordModelA,201'

@app.route('/', methods = ['GET', 'POST'])
def configure():
    form = ConfigureForm()

    if request.method == 'POST':
##        print 'This was a post'
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('t-config.html', form = form)
        else:
##            return render_template('success.html')
            cfg_tuple[0][1] = form.mode.data
            cfg_tuple[1][1] = form.tl_rate.data
            cfg_tuple[2][1] = form.g2y_dist.data
            cfg_tuple[3][1] = form.y2r_dist.data
            cfg_tuple[4][1] = form.hyst.data
            cfg_tuple[5][1] = form.sats_rate.data
            cfg_tuple[6][1] = form.test_red.data
            cfg_tuple[7][1] = form.test_yellow.data
            cfg_tuple[8][1] = form.test_green.data

##            print cfg_tuple
            save_base(cfg_tuple)

            queue.put(cfg_tuple)

            return render_template('t-config.html', form = form)

    elif request.method == 'GET':
##        print 'This was a get'
        form.mode.data = cfg_tuple[0][1]
        form.tl_rate.data = cfg_tuple[1][1]
        form.g2y_dist.data = cfg_tuple[2][1]
        form.y2r_dist.data = cfg_tuple[3][1]
        form.hyst.data = cfg_tuple[4][1]
        form.sats_rate.data = cfg_tuple[5][1]

        queue.put(cfg_tuple)

        return render_template('t-config.html', form = form)

if __name__ == '__main__':
    cfg_tuple = get_base()

    queue = Queue()
    queue.put(cfg_tuple)

    amok_thread = threading.Thread(target = run_amok, args = [queue])
    amok_thread.start()

    app.run(host='0.0.0.0', port=80, debug=False)

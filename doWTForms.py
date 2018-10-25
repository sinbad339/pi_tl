#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jdilorenzo
#
# Created:     11/09/2018
# Copyright:   (c) jdilorenzo 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from flask import Flask, render_template, request, flash
from forms import ContactForm

app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/', methods = ['GET', 'POST'])
##def contact():
def contact():
    form = ContactForm()

    if request.method == 'POST':
        print 'This was a post'
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form = form)
        else:
            return render_template('success.html')
    elif request.method == 'GET':
        print 'This was a get'
        form.name.data = "asdfjkl;"
        form.Gender.data = 'F'
        return render_template('contact.html', form = form)

if __name__ == '__main__':
##    app.run(debug = True)
    app.run(host='0.0.0.0', port=80, debug=True)

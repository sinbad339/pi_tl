from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def my_form():
    return render_template('my-form.html', tl_rate = 'hope?')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text

if __name__ == "__main__":
#   app.run(host='0.0.0.0', port=80, debug=True)
   app.run(host='0.0.0.0', port=80, debug=True)

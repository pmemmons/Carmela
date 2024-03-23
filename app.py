from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greet')
def greet():
    return 'This is a special message for Carmela!'

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Carmela! Click <a href="/greet">here</a> to see a message from me.</h1>'

@app.route('/greet')
def greet():
    return '<h1>Hello, my dear Carmela! I love you so much! 💖</h1>'

if __name__ == '__main__':
    app.run(debug=True)

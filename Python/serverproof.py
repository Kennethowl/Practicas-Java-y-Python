from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return 'I belong to Jesus, my guide in this life'

@app.route('/form')
def form():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug = True, port = 8000)
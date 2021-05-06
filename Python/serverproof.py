from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return  'CASTLEVANIA'

@app.route('/about')
def about():
    return 'I belong to Jesus, my guide in this life'

@app.route('/prueba')
def prueba():
    return 'Estamos haciendo otra prueba'

if __name__ == '__main__':
    app.run(debug = True, port = 8000)
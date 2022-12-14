from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return '<h1>Helloo World </h1>'

@app.route('/new')
def new2():
    return '<h1>Akkiiiii </h1>'

app.run()
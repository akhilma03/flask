from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/profile/<usr>')
def profile(usr):
    return render_template('prof.html',usr=usr,isActive=False)

@app.route('/book')
def Book():
    book=[{'name':'Alcamist','Author':'Paulo Coelo','Cover':'https://kbimages1-a.akamaihd.net/32ad8373-9cc5-4c4f-aa82-8155edbc7029/353/569/90/False/the-alchemist-a-graphic-novel.jpg'},{'name':'Atomic Habit','Author':'James Clear','Cover':'https://kbimages1-a.akamaihd.net/32ad8373-9cc5-4c4f-aa82-8155edbc7029/353/569/90/False/the-alchemist-a-graphic-novel.jpg'},{'name':'Discpline Eqal Freedom','Author':'Joco Willink','Cover':'https://kbimages1-a.akamaihd.net/32ad8373-9cc5-4c4f-aa82-8155edbc7029/353/569/90/False/the-alchemist-a-graphic-novel.jpg'}]
    return render_template('book.html',book=book)


app.run(debug=True)
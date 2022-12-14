from flask import Flask

new=Flask(__name__)

@new.route('/profile/<usr>')
def profile(usr):
    return '<h1> Hello %s </h1>' % usr

new.run()

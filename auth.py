from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/Login')
def login():                              # you can write the anything at last on the page you have to write the route and not this so that you will see the return one !
    return "<p>Login</p>"

@auth.route('/Logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/Sign-up')
def sign_up():
    return "<p>Sign Up</p>"
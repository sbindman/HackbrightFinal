import random
import model
import os
from flask import Flask, request, render_template, jsonify, session, flash
from selenium import webdriver


app = Flask(__name__)
app.secret_key = '\xf5!\x07!qttt\xa4\x08\xc6\xf8\n\x8a\x95m\xe2\x04g\xbb\x98|U\xa2f\x03'


@app.route('/')
def index():
    """Show map page."""
    return render_template("map.html")



@app.route('/testing')
def testing():
    """Show our index page."""
    return render_template("testing.html")



@app.route('/sign_up', methods=["GET", "POST"])
def process_signup():
	"""Show users ability to sign up or login"""

	email = request.form.get('email');
	password = request.form.get('password');

	if email:
		new_user = model.User(email=email, password=password)
		model.session.add(new_user)
		model.session.commit()
		session['email'] = email	

	return render_template("signup.html")



@app.route('/login', methods=["GET", "POST"])	
def process_login():
	"""Allow a user to login"""

	email2 = request.form.get('email')
	password2 = request.form.get('password')
	note = ""

	print "email and pass", email2, password2
	
	if email2:
		user = model.get_user(email2, password2)
		#if user is correctly identified in the system
		if user == True:
			session['email'] = email2
			note = "Welcome %s" %(email2)
		else: #bad password
			note = "Please make sure you correctly entered your email and password"

	return render_template("login.html")



@app.route('/testing')
def tests():
	"""This route is used for testing javascript / jasmine code"""

	return render_template("testing.html")



if __name__ == "__main__":
    app.run( debug=True)
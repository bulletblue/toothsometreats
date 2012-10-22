from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, jsonify
import re
from utils import mail

app = Flask(__name__)
app.secret_key = ''

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	print DATABASE
	return render_template('about.html')

@app.route('/order_form')
def order_form():
	return render_template('order_form.html')

@app.route('/photos')
def photos():
	return render_template('photos.html')

@app.route('/blog')
def blog():
	return render_template('blog.html')

@app.route('/test')
def test():
	return render_template('test.html')

@app.route('/_validate')
def validate():
	name = request.args.get('name', '', type=str)
	email = request.args.get('email', '', type=str)
	body = request.args.get('body', '', type=str)

	if name == '' or email == '' or body == '':
		return jsonify(err='Please enter all details below')
	elif not re.match('[\w.]*@[\w]*.[\w]*', email):
		return jsonify(err='Invalid email address')
	else:
		mail.send(name,email,body)
		flash('Your request has been sent, thank you!')
		return jsonify(err='NONE')

if __name__ == '__main__':
	app.run(debug = True)
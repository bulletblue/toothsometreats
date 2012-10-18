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
	return render_template('about.html')

@app.route('/order_form')
def order_form():
#	error = None
#	if request.method == 'POST':
#		if request.form['name'] == '':
#			error = 'Please enter your name'
#		elif not re.match('[\w.]*@[\w]*.[\w]*',request.form['email']):
#			error = 'Invalid Email Address'
#		elif request.form['body'] == '':
#			error = 'Please enter details'
#		else:
#			mail.send(request.form['name'], request.form['email'], request.form['body'])
#			flash('Sent!')
#			return redirect(url_for('index'))
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
	return jsonify(error='test')
#	
#	if name == '' or email == '' or body == '':
#		return jsonify(error='Please enter details below')
#	elif not re.match('[\w.]*@[\w]*.[\w]*', email):
#		return jsonify(error='Invalid email address')
#	else:
#		flash('Your request has been sent, thank you!')
#		return redirect(url_for('index'))


@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

if __name__ == '__main__':
	app.run(debug = True)
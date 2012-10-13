from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import re

#comment test
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/order_form', methods=['GET','POST'])
def order_form():
	error = None
	if request.method == 'POST':
		if not re.match('[\w.]*@[\w]*.[\w]*',request.form['email']):
			error = 'Invalid Email Address'
		elif request.form['body'] == '':
			error = 'Please enter details'
		else:
			flash('Sent!')
			return redirect(url_for('index'))
	return render_template('order_form.html', error=error)

@app.route('/photos')
def photos():
	return render_template('photos.html')

@app.route('/blog')
def blog():
	return render_template('blog.html')

if __name__ == '__main__':
	app.run()
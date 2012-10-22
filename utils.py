import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os

class Mail:

	def __init__(self):
		self.gmail_user = ''
		self.gmail_pwd = ''

	def send(self, name, sender, body):
	   msg = MIMEMultipart()

	   msg['From'] = sender
	   msg['To'] = self.gmail_user
	   msg['Subject'] = name + ' has made an order'

	   msg.attach(MIMEText(body + '\n\n Reply: ' + sender))
	   
	   mailServer = smtplib.SMTP("smtp.gmail.com", 587)
	   mailServer.ehlo()
	   mailServer.starttls()
	   mailServer.ehlo()
	   mailServer.login(self.gmail_user, self.gmail_pwd)
	   mailServer.sendmail(sender, self.gmail_user, msg.as_string())
	   mailServer.close()

mail = Mail()
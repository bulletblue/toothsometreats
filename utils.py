import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('CONFIG.INI')

class Mail:

	def __init__(self):
		self.gmail_user = config.get('SMTP', 'USER')
		self.gmail_pwd = config.get('SMTP', 'PASS')

	def send(self, name, sender, body):
	   msg = MIMEMultipart()

	   msg['From'] = sender
	   msg['To'] = self.gmail_user
	   msg['Subject'] = name + ' has made an order'

	   msg.attach(MIMEText(body + '\n\n Reply: ' + sender))
	   
	   mailServer = smtplib.SMTP(config.get('SMTP', 'SERVER'), config.get('SMTP','PORT'))
	   mailServer.ehlo()
	   mailServer.starttls()
	   mailServer.ehlo()
	   mailServer.login(self.gmail_user, self.gmail_pwd)
	   mailServer.sendmail(sender, self.gmail_user, msg.as_string())
	   mailServer.close()

mail = Mail()
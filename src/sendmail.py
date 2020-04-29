import smtplib, ssl, sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import math, random 

def sendotp(email):
  sender_email = "mpassretrieve101@gmail.com"
  receiver_email = email
  word = 'sqlpower101'
  message = MIMEMultipart("alternative")
  message["Subject"] = "OTP Request for IceBox Password Manager"
  message["From"] = sender_email
  message["To"] = receiver_email
  digits = "0123456789"
  OTP = ""
  for i in range(4) :
    OTP += digits[math.floor(random.random() * 10)]
  OTP=str(OTP)
  text = 'Your OTP is ' +  OTP
  part1 = MIMEText(text, "plain")
  message.attach(part1)
  context = ssl.create_default_context()
  with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
      server.login(sender_email, word)
      try:
        server.sendmail(sender_email, receiver_email, message.as_string())
        return OTP
      except:
        return 'failed'
def sendpassword(email,username,password):
  sender_email = "mpassretrieve101@gmail.com"
  receiver_email = email
  word = 'sqlpower101'
  message = MIMEMultipart("alternative")
  message["Subject"] = "Password Request for IceBox Password Manager"
  message["From"] = sender_email
  message["To"] = receiver_email
  text = "Your Username Is "+username+'\n'+"Your Password Is "+password
  part1 = MIMEText(text, "plain")
  message.attach(part1)
  context = ssl.create_default_context()
  with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
      server.login(sender_email, word)
      try:
        server.sendmail(sender_email, receiver_email, message.as_string())
      except:
        pass




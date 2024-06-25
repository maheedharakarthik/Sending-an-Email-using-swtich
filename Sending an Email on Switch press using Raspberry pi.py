import smtpli
from time import sleep
import RPI.GPIO as GPIO
from sys import exit

from_email = '<my-email>'
receipients_list = ['<receipient-email>']
cc_list = []
subject = 'Hello'
message = 'switch pressed on Rasberry PI'
username = '<Gmail-username>'
password = '<password>'
server = 'smtp.gmail.com:587'

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN)

def sendmail(from_addr, to_addr_list, cc_addr_list, subject, message, password, smtpserver):
  header = 'From: %s\n' %from_addr
  header += 'To: %s\n' %','.join(to_addr_list)
  header += 'Cc: %s \n' % ','.join(cc_addr_list)
  header += 'subject: %s \n\n % subject
  message = header + message

server = smtplib.SMTP(smtpserver)
server.starttls()
server.login(login,password)
problems = server.sendmail(from_addr, to_addr_list, message)
server.quit()

whiule True:
try:
  if(GPIO.input(25) == True):
    sendmail (from_email, receipients_list,cc_list, subject, message, username, password, server)
    sleep(0.1)

expect keyboardInterrupt:
exit()

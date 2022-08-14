"""
In this we will learn how to send emails with python. Python has a built-in email module which can be used.
Why it is useful: Imagine you collected a list of email ids of potential customers of your new startup, and you
want to launch emails to all of them.

smtp allows us to create an smtp server. When ever we send an email to someone, email needs to have a server
that communicates the email to the address given. Like when we open web we need http or https, when we send email
we need smtp: SIMPLE MAIL TRANSFER PROTOCOL. We need a server that follows SMTP.

Steps to send email:
1. First we create email message object
2. Then we setup where email is from and to whom email is to be sent. We set 'from' key and 'to' key in the email
object created
3. Then we setup the subject of the email. It can be done by setting up 'subject' key of the email object created
4. Then we can set the content of email using emailobject.set_content('')
This creates the email now we need our SMTP server to login to our gmail account and send this email
standard port for smtp = 587, host varies from client to client
5. open a SMTP Sever with a host and port using: with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp
6. Then we need to introduce the sending and receiving servers to each other. Using smtp.ehlo()
7. Then we use smtp.starttls(). tls is an encryption method. This command is used to securely connect with the
email client.
8. After connecting with client we need to login to client with an user and password. This is done by smtp.login().
Here we used gmail which doesnot allows to connect to the account with normal password. We need to setup an app password
for the account and use that password to login.
9. to send the email we use smtp.send_message(emailobject) and pass the email object created as an argument
"""

import smtplib
import config
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Ashish Chawla'
email['to'] = 'pythonkatappa@mailinator.com'
email['subject'] = 'You won a free subscription of Study With Ashish'
email.set_content('I am a Python Master!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()  # it is an encryption method used to securely connect with email client
    smtp.login(user=config.username, password=config.password)
    smtp.send_message(email)
    print('all good boss!!')

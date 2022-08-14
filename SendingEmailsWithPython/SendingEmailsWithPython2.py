"""
Here we are going to send html based email. We are going to replace a variable in HTML.
For this we are going to use two new built in packages:
1. Template from string module. We can substitute the $variables using .substitute.
For this we need to read this html file and convert this to a template and substitute.
To read this html file we use Path from pathlib. Path(filepath) opens the file
and Path(filepath).read_text() reads the complete file in form of string.
After that we wrap this in Template() and then we can use .substitute() to substitute variables
if the Template has multiple variables we need to use .substitute({var1: val1, var2:val2}) i.e.
pass the variables in a dict.
After that we need to set the content of the EmailMessage object and we need to tell the object
that this content is of html type by .set_content('message','html')
"""

import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

email_content = Template(Path('.\\generic_email.html').read_text())  # .substitute(name="Ashish")
email = EmailMessage()
email['from'] = 'Study With Ashish'
email['to'] = 'pythonkatappa@mailinator.com'
email['subject'] = 'Free Subscription'

email.set_content(email_content.substitute({'name': 'Katappa'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(user='noreplystudywithashish@gmail.com', password='zwhemhbfuuhaacys')
    smtp.send_message(email)

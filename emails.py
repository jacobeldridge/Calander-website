import smtplib, ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

password = "password"
context = ssl.create_default_context()
Help = MIMEMultipart('alternative')
Help['Subject'] = """\
    Here is a list of commands:
    ~log(event_name*date_time*event_desc*event_type*event_importance 1-5)
    ~display(MM/DD/YY) tells events for a specific day
    ~date() this tells todays date
    



"""
Help['From'] = "host email"
Help['To'] = "user email"

logsucc = MIMEMultipart('alternative')
logsucc['Subject'] = "Log command successful"
logsucc['From'] = "host email"
logsucc['To'] = "user email"
# Plain-text version of content

# html version of content



def sendher(whichmsg):
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login("host email", password)
        server.send_message(whichmsg)

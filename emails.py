import smtplib, ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

password = "FlashGordonFast22"
context = ssl.create_default_context()
Help = MIMEMultipart('alternative')
Help['Subject'] = """\
    Here is a list of commands:
    ~log(event_name*date_time*event_desc*event_type*event_importance 1-5)
    ~display(MM/DD/YY) tells events for a specific day
    ~date() this tells todays date
    



"""
Help['From'] = "couldbeanyone20@gmail.com"
Help['To'] = "4046554186@pm.sprint.com"

logsucc = MIMEMultipart('alternative')
logsucc['Subject'] = "Log command successful"
logsucc['From'] = "couldbeanyone20@gmail.com"
logsucc['To'] = "4046554186@pm.sprint.com"
# Plain-text version of content

# html version of content



def sendher(whichmsg):
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login("couldbeanyone20@gmail.com", password)
        server.send_message(whichmsg)
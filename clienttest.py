# server.
from imapclient import IMAPClient
import imaplib
import calfunctions
import email
from email.header import decode_header
from bs4 import BeautifulSoup
import requests
import time
import sqlite3
from sqlite3 import Error
import smtplib, ssl
import emails
me = input("user email/number")
HOST = 'imap.gmail.com'
USERNAME = input("host email")
input("Username/Email")
PASSWORD = input("password")

# authenticate

server = IMAPClient(HOST)
server.login(USERNAME, PASSWORD)
server.select_folder("INBOX")
# messages = server.search(['FROM', me])
# Start IDLE mode
server.idle()
print("Connection is now in IDLE mode, send yourself an email or quit with ^c")
while True:
    try:
        # Wait for up to 30 seconds for an IDLE response
        responses = server.idle_check(timeout=5)
        print("Server sent:", responses if responses else "nothing")
        
        if responses:
            server.idle_done()
            
            rec = server.fetch([responses[0][0]+1], ['RFC822'])
            for uid, msgdata in rec.items():
                parsedEmail = msgdata[b'RFC822']
                print(uid)
                
            msg = email.message_from_bytes(parsedEmail)
            FROM = decode_header(msg.get("From"))[0][0]
            if FROM == me:
                for part in msg.walk():
                    # extract content type of email
                    try:
                        body = part.get_payload(decode=True).decode()
                                               
                        thing = []
                        soup = BeautifulSoup(body, 'lxml')
                        row = soup.find("pre")
                        thing.append(str(row))
                        
                        simplebody = thing[0].replace("<pre>","").replace("</pre>","").replace(" ","")
                        start = thing[0].find("~") + len("~")
                        end = thing[0].find("(")
                        command = thing[0][start:end]

                        start2 = thing[0].find("(") + len("(")
                        end2 = thing[0].find(")")
                        para_whole = thing[0][start2:end2]
                        para_split = para_whole.split("*") 
                        print(command)
                        
                        if command == "log":
                            calfunctions.log(*para_split)
                            emails.sendher(emails.logsucc)
                        if command == "display":
                            calfunctions.display(para_split[0])
                            
                    except:
                        pass
            else:
                server.delete_messages(responses[0][0])
    
            
            server.idle()
            

            
            

                
    except KeyboardInterrupt:
        break

server.idle_done()
print("\nIDLE mode done")
server.logout()

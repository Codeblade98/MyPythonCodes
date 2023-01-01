from smtplib import SMTP
from email.message import EmailMessage
from string import Template 
from pathlib import Path

html = Template(Path('.\index.html').read_text())
email = EmailMessage()
email['from'] = 'agnijbiswas004@outlook.com'
email['to'] = 'destroop2@gmail.com'
email['subject'] = 'Congratulations, you are hired'
email.set_content(html.substitute(name = 'Tintin'), 'html') #to set file type as html

with SMTP(host = 'smtp-mail.outlook.com', port = 587 ) as smtp1: #use google to search ports 
    smtp1.ehlo()
    smtp1.starttls()
    smtp1.ehlo()
    smtp1.login("agnijbiswas004@outlook.com", "Ab/-101104")
    smtp1.send_message(email)
    print('All good')


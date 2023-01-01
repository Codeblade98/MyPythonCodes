#This program is not working with google or yahoo due to recent security updates
#Still works with microsoft

import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'agnijbiswas004@outlook.com'
email['to'] = 'destroop2@gmail.com'
email['subject'] = 'Congratulations, you are hired'
email.set_content('Hey we considered your application and are happy to inform on your success') 

with smtplib.SMTP(host = 'smtp-mail.outlook.com', port = 587 ) as smtp1: #use google to search ports 
    smtp1.ehlo()
    smtp1.starttls()
    smtp1.ehlo()
    smtp1.login("agnijbiswas004@outlook.com", "Ab/-101104")
    smtp1.send_message(email)
    print('All good')

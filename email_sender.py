import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Mr. Smith' #Who sent email
email['to'] = 'Mrs.Smith@gmail.com' #email address of person who will get email
email['subject'] = 'You won a 1,000,000 dollars' #topic of the letter

#Email text:
email.set_content('Congratulations, since you drank your 7,000th cup of coffee, you won our promotion and we are refunding all the money you spent on coffee.')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('youremail@gmail.com', 'Password')
    smtp.send_message(email)
    print('all done')
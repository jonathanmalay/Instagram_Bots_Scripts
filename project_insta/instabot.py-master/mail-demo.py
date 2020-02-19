import smtp
import os

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)

    subject = 'fuck me'
    body = 'dsdsdsdsds'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmailEM(EMAIL_ADDRESS,'jonathan.malai123@gmail.com',msg)


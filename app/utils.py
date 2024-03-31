from email.message import EmailMessage
# import smtplib
from django.conf import settings


def send_normal_email(data):
    email = EmailMessage(
        subject = data['email_subject'],
        body =data['email_body'],
        from_email=settings.EMAIL_HOST_USER,
        to =[data['to_email']]
    ) 
    email.send()
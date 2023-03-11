from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint


def send_mail(username, email, token):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = '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'

    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
        sib_api_v3_sdk.ApiClient(configuration))
    subject = "Account activation verification mail"
    html_content = f"<html><body><h1>This email is to activate your account by clicking this Production link: http://www.renvest.in/verify/{token} and for </br> Development use this link http://127.0.0.1:8000/verify/{token} </h1></body></html>"
    sender = {"name": "Renvest", "email": "manishsinghdewas@gmail.com"}
    to = [{"email": f"{email}", "name": f"{username}"}]
    # cc = [{"email": "example2@example2.com", "name": "Janice Doe"}]
    # bcc = [{"name": "John Doe", "email": "example@example.com"}]
    reply_to = {"email": "vishal@renvest.in", "name": "Vishal Singh"}

    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=to, reply_to=reply_to, html_content=html_content, sender=sender, subject=subject)

    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)


def send_mail_forgot_password(username, email, token):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = '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'

    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
        sib_api_v3_sdk.ApiClient(configuration))
    subject = "Account reset password mail"
    html_content = f"<html><body><h1>This email is to reset your {username} account password by clicking this Production link: http://www.renvest.in/verifyforpassword/{token} and for </br> Development use this link http://127.0.0.1:8000/verifyforpassword/{token} </h1></body></html>"
    sender = {"name": "Renvest", "email": "manishsinghdewas@gmail.com"}
    to = [{"email": f"{email}", "name": f"{username}"}]
    # cc = [{"email": "example2@example2.com", "name": "Janice Doe"}]
    # bcc = [{"name": "John Doe", "email": "example@example.com"}]
    reply_to = {"email": "vishal@renvest.in", "name": "Vishal Singh"}

    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=to, reply_to=reply_to, html_content=html_content, sender=sender, subject=subject)

    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)

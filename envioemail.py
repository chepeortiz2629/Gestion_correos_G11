from email.message import EmailMessage
import smtplib 


def enviar_email(email_destino,codigo):
    remitente="jortizh@uninorte.edu.co"
    password=" "
    destinatario=email_destino
    mensaje="hola mundo"
    email=EmailMessage()
    email['From']=remitente
    email['To']=destinatario
    email['Subject']="codigo de activación " + codigo
    email.set_content(mensaje)
    
    smtp=smtplib.SMTP("smtp-mail.outlook.com", port=587)
    smtp.starttls()
    smtp.login(remitente, password)
    smtp.sendmail(remitente, destinatario, email.as_string())
    smtp.quit()
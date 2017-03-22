import smtplib

def send_emails(emails, movie, forcast):
    #connect to the smtp server
    server = smtplib.SMTP('smtp.gmail.com', '587')
    #start the tls server
    server.starttls()
    #Login the server
    password = input("Mot de passe ?")
    from_email = 'dmakanda@activbrowser.com'
    server.login(from_email, password)

    for to_email, name in emails.items():
        message = 'Subject: Welcome ! \n'
        message += 'Hi ' + name + '!\n\n'
        message += forcast + '\n\n'
        message += movie + '\n\n'
        message += 'Hope you like it !'
        server.sendmail(from_email, to_email, message)

    server.quit()

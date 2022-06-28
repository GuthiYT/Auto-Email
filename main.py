import datetime
import smtplib
import random
import time
import schedule


def send_email():
    # Email address to send email from user to email
    user = '...@gmail.com'
    send_to = ''
    pwd = ''

    mail_text = ['']
    subject = ""

    # gets random int between first and last string in array
    random_mail_text_array = random.randint(0, len(mail_text) - 1)

    # formats to gmail compatible string
    data = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (user, send_to, subject, mail_text[random_mail_text_array - 1])

    # send message
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(user, pwd)
    server.sendmail(user, send_to, data)
    server.quit()
    return


# schedule for every day but randomise time by +-9 minutes
delay_minutes = random.randint(0, 9)
schedule.every().day.at("08:0" + delay_minutes).do(send_email)

# check if weekend
day = datetime.datetime.today().weekday()
while day != 5 or day != 6:
    schedule.run_pending()
    time.sleep(60)

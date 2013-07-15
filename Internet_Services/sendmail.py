import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

fromaddr = 'fromemailaddr'
toaddr = 'toemailaddr'
text = 'This is coding example that sends email from python, via code'
username = 'user'
password = 'pwd'
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] =  'Python 1337 stuph'
msg.attach(MIMEText(text))
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, password)
server.sendmail(fromaddr, toaddr, msg.as_string())
server.quit()

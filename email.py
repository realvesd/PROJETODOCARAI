# Enviando o email


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "re.alvesd@hotmail.com.com"
toaddr = "mailto:app.p1.unipe@gmail.com"

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = " Contatos – Aluno"

body = "Segue os contatos em anexo"

msg.attach(MIMEText(body, 'plain'))

filename = "contatos.pdf"
attachment = open(filename, "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "app.unipe2017")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

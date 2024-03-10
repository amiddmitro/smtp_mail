# Не забудьте заменить значения переменных email_user и email_password
# на свой email и пароль от почтового ящика. А также укажите корректный путь к
# файлу с вложением (attachment.txt) в переменной filename.

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import re

# Открываем файл и читаем его содержимое
with open('data1.txt', 'r') as file:
    data = file.read()

# Находим все электронные адреса, исключая "@ngs.ru" и "@admnsk.ru"
emails = re.findall(r'<([^<>]+)>', data)
filtered_emails = [email for email in emails if not email.endswith('@ngs.ru') and not email.endswith('@admnsk.ru')]

#Сохраняем в файл список адресов
file = open('emails.txt', 'w')
for email in filtered_emails:
    file.write(f'{email}, ')
file.close

# Параметры SMTP сервера
smtp_server = 'smtp.yandex.com'
port = 465  #с безопасным соединением порт 465. В случае, если вы не можете воспользоваться безопасным соединением, вы можете подключиться к SMTP-серверу по портам 25 или 587
email_user = 'Garant.ZV@yandex.ru'
email_password = 'ibmflvtbhwzcuevg' # пароль почты


# Создаем сообщение
msg = MIMEMultipart()
msg['From'] = email_user
msg['Subject'] = 'Коммерческое предложение. Ремонт подъездов. Отмостки. Кровля. тел. +7-913-940-4833'
body = 'ООО Гарант предлагает услуги по комплексному ремонту подъездов. NEW! Реставрация входных дверей.'
#body = 'Text'
msg.attach(MIMEText(body, 'plain'))

# Прикрепляем файл к сообщению
filename = 'Garant_KP.pdf'
attachment = open(filename, 'rb')
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(part)

# Отправляем письмо каждому адресу в списке
# 
for email in filtered_emails:
    msg['To'] = email
    print(email)
    print(1)
    
    server = smtplib.SMTP_SSL(smtp_server, port)
# при использовании SMTP_SSL (port 465) следующая строка отключается. Если использовать SMTP (port 587), то строка включается
#   server.starttls()   
    print(2)
    server.login(email_user, email_password)
    print(3)
    server.send_message(msg= msg, to_addrs=email)
    server.quit()

print("Emails sent successfully.")


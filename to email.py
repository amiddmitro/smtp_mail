# Не забудьте заменить значения переменных email_user и email_password
# на свой email и пароль от почтового ящика. А также укажите корректный путь к
# файлу с вложением (attachment.txt) в переменной filename.

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Открываем файл для чтения
with open("data.txt", "r") as file:
    # Читаем данные из файла
    emails = file.read().split(",")

# Параметры SMTP сервера
smtp_server = 'smtp.yandex.com'
port = 587  #с безопасным соединением порт 465. В случае, если вы не можете воспользоваться безопасным соединением, вы можете подключиться к SMTP-серверу по портам 25 или 587
email_user = 'Garant.ZV@yandex.ru'
email_password = 'ibmflvtbhwzcuevg' # пароль почты


# Создаем сообщение
msg = MIMEMultipart()
msg['From'] = email_user
msg['Subject'] = 'Коммерческое предложение. Ремонт подъездов. Отмостки. Кровля'
body = 'Фирма Гарант производит работы по ремонту подъездов МКД, ремонту и устройству отмостки, обустройство кровли. Реставрируем входные двери. Низкие цены! Смета бесплатно! Фирма Гарант предлагает взаимовыгодное сотрудничество! тел +7-913-940-4833'
#body = 'Text'
msg.attach(MIMEText(body, 'plain'))

# Прикрепляем файл к сообщению
#filename = 'Garant_KP.pdf'
#attachment = open(filename, 'rb')
#part = MIMEBase('application', 'octet-stream')
#part.set_payload((attachment).read())
#encoders.encode_base64(part)
#part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
#msg.attach(part)

# Отправляем письмо каждому адресу в списке
for email in emails:
    msg['To'] = email
    print(email)
    print(1)
    
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()
    print(2)
    server.login(email_user, email_password)
    print(3)
    server.send_message(msg, to_addrs=email)
    server.quit()

print("Emails sent successfully.")


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
smtp_server = 'smtp.yandex.ru'
port = 465
email_user = 'Garant.ZV@ya.ru'
email_password = 'ufCImpFH' # пароль почты Заитов


# Создаем сообщение
msg = MIMEMultipart()
msg['From'] = email_user
msg['Subject'] = 'Test email with attachments'
body = 'This is a test email with attachments.'
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
for email in emails:
    msg['To'] = email
#    server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
    print(f'{smtp_server}:{port}')
    with smtplib.SMTP_SSL(smtp_server, port) as server:

        server.login(email_user, email_password)
        server.send_message(msg)



#     server = smtplib.SMTP_SSL(f'{smtp_server}:{port}')
# #    server = smtplib.SMTP(smtp_server, port)
#     server.starttls()
    print(email_user, email_password  , 2)
#     server.login(email_user, email_password)
#     server.send_message(msg)
    server.quit()

print("Emails sent successfully.")


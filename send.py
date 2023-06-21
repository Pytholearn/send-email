import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, receiver_email, subject, message):
    # تنظیمات اتصال به سرور SMTP گوگل
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # ساختن پیام
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    # افزودن متن پیام
    msg.attach(MIMEText(message, "plain"))

    # برقراری ارتباط با سرور SMTP
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)

    # ارسال ایمیل
    server.send_message(msg)

    # خاتمه ارتباط با سرور SMTP
    server.quit()

# مقادیر ورودی
sender_email = "police123456789ilia@gmail.com"
sender_password = "qctkfkelxoucaweo"
receiver_email = "iliapolice123456789@gmail.com"
subject = "Hello from Python"
message = "This is a test email."

# فراخوانی تابع ارسال ایمیل
send_email(sender_email, sender_password, receiver_email, subject, message)
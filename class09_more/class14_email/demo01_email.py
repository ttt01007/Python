import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

smtpserver = "smtp.qq.com"
smtpport = 465
from_mail = "398847378@qq.com"
to_mail = ["398847378@qq.com"]
password = "lvdqwvxzbxekcaai"  # 16位授权码

subject = "test report"
from_name = "水云之外"
# from_mail = "aaaaaa@qq.com"
# to_mail = ["bbbbbb@qq.com"]
cc_mail = ["398847378@qq.com"]

msg1 = MIMEText(_text='最后一节课', _subtype='plain', _charset='utf-8')
msg = MIMEMultipart()
msg["Subject"] = Header(subject, "utf-8")
msg["From"] = Header(from_name + " <" + from_mail + ">", "utf-8")
msg["To"] = Header(",".join(to_mail), "utf-8")
msg["Cc"] = Header(",".join(cc_mail), "utf-8")
msg.attach(msg1)

try:
    smtp = smtplib.SMTP_SSL(smtpserver, smtpport)
    smtp.login(from_mail, password)
    smtp.sendmail(from_mail, to_mail, msg.as_string())
except(smtplib.SMTPException) as e:
    print(e.message)
finally:
    smtp.quit()

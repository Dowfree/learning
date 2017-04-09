#!usr/bin/enc python
# -*- coding: utf-8 -*-
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# 输入Email地址和口令:
# from_addr = input('From: ')
from_addr = '923299213@qq.com'
password = 'tumnmjvjwrmibfbi'
# password = input('Password: ')
# 输入收件人地址:
# to_addr = input('To: ')
to_addr = '923299213@qq.com'
# 输入SMTP服务器地址:
# smtp_server = input('SMTP server: ')
smtp_server = 'smtp.qq.com'

# msg = MIMEText('Hello, send by Python...', 'plain', 'utf-8')
# msg = MIMEText('<html><body><h1>Hello</h1>' +
#              '<p>send by <a href="http://www.python.org">Python</a>...</p>'
#              +
#               '</body></html>', 'html', 'utf-8')
msg = MIMEMultipart()
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理者 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候...', 'utf-8').encode()
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
with open(r'C:\Users\free\Pictures\其他\Capture001.png', 'rb') as fp:
    mime = MIMEBase('image', 'png', filename='Capture001.png')
    mime.add_header('Conntent_Disposition', 'attachment', filename='Capture001.png')
    mime.add_header('Content_ID', '<0>')
    mime.add_header('X-Attachme_Id', '0')
    mime.set_payload(fp.read())
    encoders.encode_base64(mime)
    msg.attach(mime)

server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from imapclient import IMAPClient
import StringIO
import email
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

# python 2.3.*: email.Utils email.Encoders
from email.utils import COMMASPACE,formatdate
from email import encoders

import os

hostname = 'outlook.office365.com'
username = 'puyu.chen@binqsoft.com'
password = 'Password01!'
ssl = True


def open_connection(hostname, username, password):

    connection = IMAPClient(hostname, use_uid=True, ssl=ssl)

    connection.login(username, password)
    # connection.select_folder('INBOX')
    # # connection.create_folder('test')
    # # connection.create_folder(u'测试11')
    # mailbox = u'测试11'
    # date_time = None
    # # messages = connection.search(['NOT DELETED'])
    # data = connection.fetch('2553', ['FLAGS', 'RFC822'])
    # msg = data[2553]['RFC822']
    # flags = data[2553]['FLAGS']
    # connection.append(mailbox, msg, flags, msg_time=None)
    return connection

#
# open_connection(hostname, username, password)


def send_mail(fro, to, cc, subject, text, files={}):
    """

    :param fro: 发件人
    :param to: 收件人
    :param cc: 抄送
    :param subject:  主题
    :param text: 正文
    :param files: 附件  （附件形式{文件名: 文件内容, ...}）
    :return:
    """
    # assert type(server) == dict
    # assert type(to) == list
    # assert type(files) == list

    msg = MIMEMultipart()
    msg['From'] = fro
    msg['Subject'] = subject
    msg['To'] = COMMASPACE.join(to)  # COMMASPACE==', '
    msg['cc'] = COMMASPACE.join(cc)  # COMMASPACE==', '
    msg['Date'] = formatdate(localtime=True)
    msg.attach(MIMEText(text))

    for file_name, file_content in files.iteritems():
        part = MIMEBase('application', 'octet-stream')  # 'octet-stream': binary data
        part.set_payload(file_content)
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % file_name)
        msg.attach(part)

    connection = open_connection(hostname, username, password)
    mailbox = 'INBOX'
    flags = ''
    connection.append(mailbox, msg.as_string(), flags, msg_time=None)

send_mail('zhangzinan01@126.com', ['puyu.chen@binqsoft.com'], ['745690939@qq.com'], 'Hello Word', 'text1111', {})
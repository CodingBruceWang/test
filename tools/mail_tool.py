# -*- coding: utf-8 -*-
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart, MIMEBase
from email.utils import parseaddr, formataddr
import smtplib
import logging

class MailTool(object):
    smtp_server = 'smtp.163.com'
    from_addr = user = 'wangfoqing25@163.com'
    password = 'wangfoqing25'

    def _get_smtp_server(self):
        try:
            server = smtplib.SMTP(self.smtp_server, 25)
            # 25端口连接SMTP服务器时，使用的是明文传输
            # 创建SSL安全连接加密SMTP会话
            server.starttls()
            server.set_debuglevel(1)
            server.login(self.user, self.password)
        except  Exception, e:
            logging.error('logon smtp server failed. %s' % e.message)
            return None
        return server

    # 发送普通的文本文件
    def send_mail(self, from_addr, to_addr, subject, content):
        mail_content = 'hello, send by Python...; %s' %content
        msg = MIMEText(mail_content, 'plain', 'utf-8')
        sender = u'Python爱好者 <%s>'%from_addr
        # msg['To'] = self._format_addr(u'管理员 <%s>'%to_addr)
        msg['From'] = from_addr
        msg['To'] = to_addr
        # msg['Subject'] = Header(u'来自SMTP的问候……%'%subject, 'utf-8').encode()
        # msg['Subject'] = Header(u'来自SMTP的问候……%', 'utf-8').encode()
        msg['Subject'] = Header(subject, 'utf-8').encode()

        server = self._get_smtp_server()
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()

    def _format_addr(self, s):
        name, addr = parseaddr(s)
        return formataddr(( \
            Header(name, 'utf-8').encode(), \
            addr.encode('utf-8') if isinstance(addr, unicode) else addr))

    # 发送html邮件 将MIMEText的_subtype参数更改为html
    def send_html_mail(self, from_addr, to_addr, subject, content):
        mail_content = '<html><body><h1>Hello; %s</h1>' % content + '<p>send by <a href="http://www.python.org"></a>...</p>' + '</body></html>'
        msg = MIMEText(mail_content, 'html', 'utf-8')
        msg['From'] = from_addr
        msg['To'] = to_addr
        msg['Subject'] = Header(subject, 'utf-8').encode()
        server = self._get_smtp_server()
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()

    # 带附件的邮件可以看做包含若干部分的邮件：文本和各个附件本身
    # 所以，可以构造一个MIMEMultipart对象代表邮件本身，
    # 然后往里面加上一个MIMEText作为邮件正文，
    # 再继续往里面加上表示附件的MIMEBase对象即可：
    def send_mail_with_attach(self, from_addr, to_addr, subject, content):
        # 邮件对象:
        msg = MIMEMultipart()
        from_addr = 'Python爱好者<%s>' % from_addr
        to_addr = '管理员<%s>' % to_addr
        msg['From'] = self._format_addr('Python爱好者<wangfoqing25@163.com>')
        msg['To'] = self._format_addr(to_addr)
        msg['Subject'] = Header(subject, 'utf-8').encode()

        # 邮件正文是MIMEText:
        msg.attach(MIMEText(content, 'plain', 'utf-8'))

        # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
        with open('/home/wfq/ops/static/image/qicheng.jpg', 'rb') as f:
            # 设置附件的MIME和文件名，这里是png类型:
            mime = MIMEBase('image', 'jpg', filename='qicheng.jpg')
            # 加上必要的头信息:
            mime.add_header('Content-Disposition', 'attachment', filename='qicheng.jpg')
            mime.add_header('Content-ID', '<0>')
            mime.add_header('X-Attachment-Id', '0')
            # 把附件的内容读进来:
            mime.set_payload(f.read())
            # 用Base64编码:
            encoders.encode_base64(mime)
            # 添加到MIMEMultipart:
            msg.attach(mime)
            server = self._get_smtp_server()
            server.sendmail(from_addr, [to_addr], msg.as_string())
            server.quit()
        return ''

    # 要把图片嵌入到邮件正文中，我们只需按照发送附件的方式，先把邮件作为附件添加进去，然后，在HTML中通过引用src = "cid:0"
    # 就可以把附件作为图片嵌入了。如果有多个图片，给它们依次编号，然后引用不同的cid:x即可。
    def send_mail_with_image(self, from_addr, to_addr, subject, content):
        # 邮件对象:
        msg = MIMEMultipart()
        from_addr = 'Python爱好者<%s>' % from_addr
        to_addr = '管理员<%s>' % to_addr
        msg['From'] = self._format_addr('Python爱好者<wangfoqing25@163.com>')
        msg['To'] = self._format_addr(to_addr)
        msg['Subject'] = Header(subject, 'utf-8').encode()

        # 邮件正文是MIMEText:
        mail_content = '<html><body><h1>Hello %s </h1>' + '<p><img src="cid:0"></p>' + '</body></html>'%content
        msg.attach(MIMEText(mail_content, 'html', 'utf-8'))

        # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
        with open('/home/wfq/ops/static/image/qicheng.jpg', 'rb') as f:
            # 设置附件的MIME和文件名，这里是png类型:
            mime = MIMEBase('image', 'jpg', filename='qicheng.jpg')
            # 加上必要的头信息:
            mime.add_header('Content-Disposition', 'attachment', filename='qicheng.jpg')
            mime.add_header('Content-ID', '<0>')
            mime.add_header('X-Attachment-Id', '0')
            # 把附件的内容读进来:
            mime.set_payload(f.read())
            # 用Base64编码:
            encoders.encode_base64(mime)
            # 添加到MIMEMultipart:
            msg.attach(mime)
            server = self._get_smtp_server()
            server.sendmail(from_addr, [to_addr], msg.as_string())
            server.quit()
        return ''
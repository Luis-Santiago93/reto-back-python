import os
import smtplib, ssl
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from settings import create_app, ENVIRONMENT_NAME, config_by_name

app = create_app(ENVIRONMENT_NAME)
config = config_by_name[ENVIRONMENT_NAME]


class email_service:

    def __init__(self, template_name=None):
        self.server = app.config['EMAIL_SERVER']
        self.port = app.config['EMAIL_PORT']
        self.sender_email = app.config['EMAIL_SENDER']
        self.password = app.config['EMAIL_PASSWORD']
        self.context = ssl.create_default_context()

        filename = os.path.join(app.static_folder, template_name)
        with open(filename, 'r', encoding='utf-8') as f:
            self.html_template = f.read()

    def send_email(self, params, subject, receiver_email):
        message = MIMEMultipart("related")
        message["Subject"] = subject
        message["From"] = self.sender_email

        for key in params:
            self.html_template = self.html_template.replace(f'[{key}]', params[key])

        body = MIMEText(self.html_template, "html")
        message.attach(body)

        logo_path = os.path.join(app.static_folder + '/img/', 'logo.png')
        fp = open(logo_path, 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()

        msgImage.add_header('Content-ID', '<logo>')
        message.attach(msgImage)

        pemex_path = os.path.join(app.static_folder + '/img/', 'pemex.png')
        fpp = open(pemex_path, 'rb')
        msgImage2 = MIMEImage(fpp.read())
        fpp.close()

        msgImage2.add_header('Content-ID', '<pemex>')
        message.attach(msgImage2)

        with smtplib.SMTP_SSL(self.server, self.port) as server:
            server.login(self.sender_email, self.password)
            email_list = list(set(receiver_email.split(";")))
            len_email_list = len(email_list)
            set_num = config.EMAIL_RECIPIENTS_NUMBER

            for i in range(0, len_email_list, set_num):
                receiver_email = "BCC: %s\r\n" % ";".join(email_list[i:i + 1 * set_num])
                server.sendmail(self.sender_email, receiver_email, message.as_string())

            server.quit()

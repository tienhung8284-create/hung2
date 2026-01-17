import smtplib
from dotenv import load_dotenv

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import json
from jinja2 import Template

load_dotenv()

# 1. Load template HTML
template_str = open("module3/SS5/emails_template/html_template/giaybaoduthi.html", encoding="utf-8").read()
template = Template(template_str)

# 2. Load danh sách học sinh (list JSON)
def load_user(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        print("Không có file JSON")
        return []

receiver_list = load_user("C:\pythonlevel2\module3\giaybaoduthi.json")

# 3. Config mail
sender = os.getenv('FROM_EMAIL')
password = os.getenv('APP_PASSWORD')
subject = os.getenv('SUBJECT')

# 4. Gửi mail từng học sinh
if receiver_list:
    for load_data in receiver_list:

        # Render HTML
        email_html_content = template.render(**load_data)

        # Lấy email người nhận
        receiver_email = load_data.get("email")

        if not receiver_email:
            print("Bỏ qua: thiếu email")
            continue

        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = receiver_email

        part_html = MIMEText(email_html_content, 'html', 'utf-8')
        msg.attach(part_html)

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(sender, password)
                server.sendmail(sender, receiver_email, msg.as_string())
            print(f"Đã gửi thành công: {receiver_email}")

        except Exception as e:
            print(f"Lỗi gửi email cho {receiver_email}: {e}")

else:
    print("Không có dữ liệu")
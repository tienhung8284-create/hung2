import smtplib
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os 
import json
from jinja2 import Template

load_dotenv()

#1: Lấy template
template_str = open('C:\pythonlevel2\module3\SS6\homework\emails_template\html_template/bangdiem.html','r',encoding='utf-8').read()
template = Template(template_str)

#2: Đọc dữ liệu người dùng
def load_user(file_path):
    try:
        with open(file_path,'r',encoding='utf-8') as f:
            return json.load(f)
    except:
        print('Không có file JSON')
        return []
    
receiver_data = load_user('C:\pythonlevel2\module3\SS6\homework\student_data.json')

#3: Khởi tạo cấu hình gửi mail
sender = os.getenv('FROM_EMAIL')
password = os.getenv('APP_PASSWORD')
subject = os.getenv('SUBJECT')

#4: Vòng lặp và gửi email
if receiver_data:
    for load_data in receiver_data:
        email_html_content = template.render(**load_data)
        receiver_data = load_data.get('email')

        if not receiver_data:
            print('Bỏ qua email thiếu địa chỉ.')
            continue

        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = receiver_data

        # Thêm nội dung html
        part_html = MIMEText(email_html_content,'html','utf-8')
        msg.attach(part_html)

        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(sender,password)
                server.sendmail(sender,receiver_data,msg.as_string())
                print(f'Đã gửi thành công {receiver_data}')
        except Exception as e:
            print(f'Lỗi gửi email cho {receiver_data}', e)
else:
    print('Không có dữ liệu')


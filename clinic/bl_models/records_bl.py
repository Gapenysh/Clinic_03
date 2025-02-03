import logging
import smtplib
from email.mime.text import MIMEText

from clinic.config import settings

class RecordBL(object):
    @staticmethod
    def create_record(data):
        try:
            # Отправка данных на почту
            msg = MIMEText(f"Новая заявка на запись:\nФамилия: {data['last_name']}\nИмя: {data['first_name']}\nДата рождения: {data['birth_date']}\nНомер телефона: {data['phone_number']}\nСпециальность: {data.get('speciality', 'Не указана')}")
            msg['Subject'] = 'Новая заявка на запись'
            msg['From'] = 'yazik_2018@mail.ru'
            msg['To'] = 'abdullinramzil4@gmail.com'

            with smtplib.SMTP('smtp.mail.ru', 587) as server:
                server.starttls()
                server.login('yazik_2018@mail.ru', f'{settings.PASSWORD_BY_MAIL}')
                server.sendmail('yazik_2018@mail.ru', ['abdullinramzil4@gmail.com'], msg.as_string())
                print("Письмо успешно отправлено!")

            return True, None
        except Exception as e:
            logging.error(f"Error sending email: {e}")
            return False, str(e)
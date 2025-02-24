import logging
import smtplib
from email.mime.text import MIMEText

from clinic.config import settings

class RecordBL(object):
    @staticmethod
    def create_record(data):
        try:
            # Создание HTML-сообщения с вертикальной таблицей и разделительными линиями
            html_content = f"""
                    <!DOCTYPE html>
                    <html lang="ru">
                    <head>
                        <meta charset="UTF-8">
                        <title>Новая заявка</title>
                    </head>
                    <body style="margin: 0; padding: 0; background-color: #f4f4f4; text-align: center;">
                        <table width="100%" cellspacing="0" cellpadding="0" border="0" style="background-color: #f4f4f4; padding: 20px 0;">
                            <tr>
                                <td align="center">
                                    <table width="270" cellspacing="0" cellpadding="8" border="0" style="background-color: #ffffff; border: 1px solid #cccccc;">
                                        <tr>
                                            <th colspan="2" style="text-align: center; font-size: 18px; color: #4B0082; padding: 15px 20px;">Новая заявка</th>
                                        </tr>

                                        <!-- Имя -->
                                        <tr>
                                            <td colspan="2" style="font-size: 14px; font-weight: bold; color: #333; padding: 6px 20px 3px;">Имя</td>
                                        </tr>
                                        <tr>
                                            <td colspan="2" style="font-size: 14px; color: #333; padding: 3px 20px 6px;">{data['first_name']} {data['last_name']}</td>
                                        </tr>

                                        <!-- Разделительная линия -->
                                        <tr>
                                            <td colspan="2" align="center" style="padding: 6px 20px;">
                                                <hr style="border: none; border-top: 1px solid #cccccc; margin: 0;">
                                            </td>
                                        </tr>

                                        <!-- Дата рождения -->
                                        <tr>
                                            <td colspan="2" style="font-size: 14px; font-weight: bold; color: #333; padding: 6px 20px 3px;">Дата рождения</td>
                                        </tr>
                                        <tr>
                                            <td colspan="2" style="font-size: 14px; color: #333; padding: 3px 20px 6px;">{data['birth_date']}</td>
                                        </tr>

                                        <!-- Разделительная линия -->
                                        <tr>
                                            <td colspan="2" align="center" style="padding: 6px 20px;">
                                                <hr style="border: none; border-top: 1px solid #cccccc; margin: 0;">
                                            </td>
                                        </tr>

                                        <!-- Номер -->
                                        <tr>
                                            <td colspan="2" style="font-size: 14px; font-weight: bold; color: #333; padding: 6px 20px 3px;">Номер</td>
                                        </tr>
                                        <tr>
                                            <td colspan="2" style="font-size: 14px; padding: 3px 20px 6px;">
                                                <a href="tel:{data['phone_number']}" style="color: #0081ec; text-decoration: underline;">{data['phone_number']}</a>
                                            </td>
                                        </tr>

                                        <!-- Разделительная линия -->
                                        <tr>
                                            <td colspan="2" align="center" style="padding: 6px 20px;">
                                                <hr style="border: none; border-top: 1px solid #cccccc; margin: 0;">
                                            </td>
                                        </tr>

                                        <!-- Специалисты -->
                                        <tr>
                                            <td colspan="2" style="font-size: 14px; font-weight: bold; color: #333; padding: 6px 20px 3px;">Специалисты</td>
                                        </tr>
                                        <tr>
                                            <td colspan="2" style="font-size: 14px; color: #333; padding: 3px 20px 15px;">{data.get('speciality', 'Не указана')}</td>
                                        </tr>
                                    </table>

                                    <p style="color: grey; font-size: 12px; margin-top: 10px;">Отправлено с <span style="text-decoration: underline;">Clinic 03</span></p>
                                </td>
                            </tr>
                        </table>
                    </body>
                    </html>
                    """

            msg = MIMEText(html_content, 'html')
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
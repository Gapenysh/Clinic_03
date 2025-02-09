import logging
import smtplib
from email.mime.text import MIMEText

from clinic.config import settings

class RecordBL(object):
    @staticmethod
    def create_record(data):
        try:
            # Создание HTML-сообщения
            html_content = f"""
            <!DOCTYPE html>
            <html lang="en">
              <head>
                <meta charset="UTF-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <title>Document</title>
                <style>
                  body {{
                    margin: 0;
                  }}
                  .main {{
                    height: 100vh;
                    background-color: #d4d4d4;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    flex-direction: column;
                    gap: 20px;
                  }}

                  .form {{
                    background-color: white;
                    width: 200px;
                    display: flex;
                    justify-content: center;
                    flex-direction: column;
                    align-items: center;
                    gap: 10px;
                    padding: 40px 20px;
                    border: 1px solid grey;
                  }}

                  .field {{
                    width: 90%;
                    border-bottom: 1px solid black;
                  }}

                  .phone {{
                    text-decoration: underline;
                    color: #0081ec;
                  }}

                  .logo {{
                    width: 101px;
                  }}

                  h1 {{
                    font-size: 15px;
                    font-weight: 600;
                    margin: 5px 0;
                  }}

                  p {{
                    font-size: 13px;
                    margin: 5px 0;
                  }}

                  .clinic {{
                    color: grey;
                    font-size: 12px;
                  }}

                  .link {{
                    display: inline;
                    text-decoration: underline;
                  }}
                </style>
              </head>
              <body>
                <main class="main">
                  <div class="form">
                    <img class="logo" src="./images/clinica03.png" alt="" />
                    <div class="field">
                      <h1>Имя</h1>
                      <p>{data['first_name']} {data['last_name']}</p>
                    </div>
                    <div class="field">
                      <h1>Дата рождения</h1>
                      <p>{data['birth_date']}</p>
                    </div>
                    <div class="field">
                      <h1>Номер</h1>
                      <p class="phone">{data['phone_number']}</p>
                    </div>
                    <div class="field">
                      <h1>Специалисты</h1>
                      <p>{data.get('speciality', 'Не указана')}</p>
                    </div>
                  </div>
                  <div class="clinic">
                    Отправлено с
                    <p class="link">Clinic 03</p>
                  </div>
                </main>
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
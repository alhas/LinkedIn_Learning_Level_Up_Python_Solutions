import smtplib

subject = 'Subject of the email'
message = f'Subject: {subject}\n\n"Hello World!"'
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login('bahtiyaralialhas@gmail.com', 'etdi wjmk herw uyrt')
    server.sendmail('bahtiyaralialhas@gmail.com', 'alhas@outlook.com', message)





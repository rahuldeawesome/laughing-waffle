import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s=starttls()
s.login("rahulsunny0106@gmail.com","Rahul3108")
message="yo yo"
s.sendmail("rahulsunny0106@gmail.com","rahulsunny86@gmail.com",message)
s.quit()

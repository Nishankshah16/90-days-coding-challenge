# https://docs.python.org/3/library/smtplib.html        --smtp docs
# https://docs.python.org/3/library/datetime.html       --datetime docs
# https://www.positivityblog.com/monday-motivation-quotes/      --monday motivation quotes
# https://www.pythonanywhere.com/                       -- host code on cloud

import smtplib
import datetime
import random

my_email=""
my_password=""
# with smtplib.SMTP("smtp.mail.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email,password=my_password)
#     connection.sendmail(from_addr=my_email,to_addrs="anunita.n@gmail.com",msg="Subject: Nonsense \n\n Anuja pagal hai")

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
now = datetime.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("/Users/nishanknitinshah/Documents/Python/90 DAYS OF PYTHON/DAY32_email_smtp/quotes.txt") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=my_password)
        connection.sendmail(from_addr=my_email,to_addrs="anunita.n@gmail.com",msg=f"Subject: {days[weekday]} Motivation \n\n{quote}")
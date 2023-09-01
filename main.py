
#  10% done - Sending emails with smtplib:
# import smtplib
#
# my_email = "wanyudevtest@gmail.com"
# password = "btbgsmumwrcsdivg"
# receiver = "wanyudevtest@yahoo.com"
#
# # This method could be optimized as second down below:
# # connection = smtplib.SMTP("smtp.gmail.com", port=587)
# # connection.starttls()
# # connection.login(user=my_email, password=password)
# # connection.sendmail(from_addr=my_email,
# #                     to_addrs=receiver,
# #                     msg="Subject:Hi there!\n\nThis is a test to see if sending email works")
# # connection.close()
#
#
# # Optimized method: to close it automatically
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs=receiver,
#                         msg="Subject:Hi there!\n\nThis is a test to see if sending email works"
#                         )


# # 20% done - Working with the datetime Module:
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# # print(now)
# # print(year)
# # print(type(now))
# # print(day_of_week)
#
# # when harver over, it says hour=..., it means it was set to have a default:
# date_of_birth = dt.datetime(year=1989, month=1, day=26)
# print(date_of_birth)
# # Output: 1989-01-26 00:00:00, which means 00:00:00 is default number



# # 30% done - Send Motivational Quotes on Mondays via Email:
# import datetime as dt
# import random
# import smtplib
#
# MY_EMAIL = "wanyudevtest@gmail.com"
# PASSWORD = "btbgsmumwrcsdivg"
# RECEIVER = "wanyudevtest@yahoo.com"
#
# now = dt.datetime.now()
# day_of_week = now.weekday()
#
# if day_of_week == 3:    # we are test it now on Thursday
#     with open("quotes.txt", "r") as file:
#         lines = file.readlines()
#         body_text = random.choice(lines)
#     # print(type(lines))
#     # print(lines)
#     # print(body_text)
#
#     with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#         connection.starttls()
#         connection.login(user=MY_EMAIL, password=PASSWORD)
#         connection.sendmail(from_addr=MY_EMAIL,
#                             to_addrs=RECEIVER,
#                             msg=f"Subject:Happy Monday, let's rock n roll!\n\n"
#                                 f"Hi Winnie,\n\n{body_text}\n"
#                                 f"May You Have a great week :)\n\n"
#                                 f"Wan-Yu"
#                             )


# 40% done - Automated Birthday Wisher Project

import datetime as dt
import random
import smtplib
import pandas
import os

MY_EMAIL = "wanyudevtest@gmail.com"
PASSWORD = "btbgsmumwrcsdivg"
FOLDER_PATH = "letter_templates"
TXT_FILES = [file for file in os.listdir(FOLDER_PATH)
             if file.endswith(".txt")]

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day

file = pandas.read_csv("birthdays.csv")
# print(file)
# print(file.to_dict(orient="records"))
data = file.to_dict()
# print(data)
# print(data["year"])
for _ in data:
    if data["year"] == year and data["month"] and data["day"]:
        receiver = data["email"]
        name = data["name"]

        random_file = random.choice(TXT_FILES)
        file_path = os.path.join(FOLDER_PATH, random_file)
        with open(file_path, "r") as file:
            template = file.readlines()

            # print(template)
            # Not sure why it's not printing out yet.



        # with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        #     connection.starttls()
        #     connection.login(user=MY_EMAIL, password=PASSWORD)
        #     connection.sendmail(from_addr=MY_EMAIL,
        #                         to_addrs=receiver,
        #                         msg=f"Subject:Happy Birthday, {name}!\n\n)




# if
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=MY_EMAIL, password=PASSWORD)
#     connection.sendmail(from_addr=MY_EMAIL,
#                         to_addrs=RECEIVER,
#                         msg=f"Subject:Happy Monday, let's rock n roll!\n\n"
#                             f"Hi Winnie,\n\n{body_text}\n"
#                             f"May You Have a great week :)\n\n"
#                             f"Wan-Yu"
#                         )


# with open("quotes.txt", "r") as file:
#     lines = file.readlines()
#     body_text = random.choice(lines)
# # print(type(lines))
# # print(lines)
# # print(body_text)
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=MY_EMAIL, password=PASSWORD)
#     connection.sendmail(from_addr=MY_EMAIL,
#                         to_addrs=RECEIVER,
#                         msg=f"Subject:Happy Monday, let's rock n roll!\n\n"
#                             f"Hi Winnie,\n\n{body_text}\n"
#                             f"May You Have a great week :)\n\n"
#                             f"Wan-Yu"
#                         )








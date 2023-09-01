
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


# 20% done - Working with the datetime Module:
import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
# print(now)
# print(year)
# print(type(now))
# print(day_of_week)

# when harver over, it says hour=..., it means it was set to have a default:
date_of_birth = dt.datetime(year=1989, month=1, day=26)
print(date_of_birth)
# Output: 1989-01-26 00:00:00, which means 00:00:00 is default number





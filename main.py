import smtplib


my_email = "wanyudevtest@gmail.com"
password = "btbgsmumwrcsdivg"
receiver = "wanyudevtest@yahoo.com"

# This method could be optimized as second down below:
# connection = smtplib.SMTP("smtp.gmail.com", port=587)
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email,
#                     to_addrs=receiver,
#                     msg="Subject:Hi there!\n\nThis is a test to see if sending email works")
# connection.close()


# Optimized method: to close it automatically
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=receiver,
                        msg="Subject:Hi there!\n\nThis is a test to see if sending email works"
                        )




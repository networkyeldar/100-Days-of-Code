import random
import smtplib
import pandas
import datetime as dt
import random
my_email = "eltaiuly1205@gmail.com"
password = "mzymtbymhzfnslga"



today_tuple = (dt.datetime.now().month,dt.datetime.now().day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_{random.randint(1,3)}.txt"
    with open(file_path) as file:
        contents = file.read()
        new_content = contents.replace("[NAME]",birthday_person["name"])

    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"], msg=f"Subject: Happy Birthday!!!\n\n{new_content}")
    connection.close()





# import pywhatkit
#
# # Defining the Phone Number and Message
# phone_number = "+77014933332"
# message = "Hello"
#
# # Sending the WhatsApp Message
# pywhatkit.sendwhatmsg_instantly(phone_number, message)
#
# # Displaying a Success Message
# print("WhatsApp message sent!")

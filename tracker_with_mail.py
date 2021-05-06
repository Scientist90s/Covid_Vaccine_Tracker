# This program basically sends an email whenever vaccine slot is available in the specified pincodes

import requests
import json
from datetime import date
import smtplib, ssl
import time

# you can specify all the pincodes here
pin = ["380008", "382443", "380050", "380015"]
cur_date = date.today()

smtp_server = "smtp.gmail.com"  # smtp server
port = 587
sender_email = "gcet.mechatronics@gmail.com"    # sender's email address
receiver_email = "yshethwala@gmail.com"   #  receiver's email address
password = input("Type your password and press enter: ")
context = ssl.create_default_context()
message = ""

mail_flag = True

# this function uses COWIN API to get data of available slots of vaccine
def calendarbyPIN(pincode, date):
    global mail_flag
    global message
    message = ""
    URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin"
    pin = pincode
    date = date
    cnt = 0

    for code in pin:
        params = {"pincode":code, "date":date}
        response = requests.get(URL, params)
        if response.ok:
            data = json.loads(response.text)
            # print(data)
            if data["centers"]:
                for center in data["centers"]:
                    for session in center["sessions"]:
                        if(session["min_age_limit"]<45 and session["available_capacity"]>0):
                            cnt += 1
                            message += "\n"
                            message += "Center Name: "+str(center["name"])
                            message += "Pincode: "+str(center["pincode"])
                            message += "Date: "+str(session["date"])
                            message += "Available capacity: "+str(session["available_capacity"])
                            message += "\n"
            # else:
            #     print("No centers found")

    if cnt > 0:
        if mail_flag == True:
            message = "Slots available book as soon as possible\n\n"+message
            message = "Subject: Vaccine Slot Available\n\n"+message
            send_email(message)
            mail_flag = False
    else:
        if mail_flag == False:
            mail_flag = True

# This fucntion sends email
def send_email(msg):
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg)
    except Exception as e:
        print(e)
    finally:
        server.quit()

if __name__=="__main__":
    while True:
        calendarbyPIN(pin, cur_date.strftime("%d-%m-%Y"))
        time.sleep(60*5)
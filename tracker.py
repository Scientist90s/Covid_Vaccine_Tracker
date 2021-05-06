# This program will tell you if the slot is available or not in the specified pincodes

import requests
import json
from datetime import date
import smtplib
import ssl

pin = ["380008", "382443", "380050", "380015"]
cur_date = date.today()


def calendarbyPIN(pincode, date):
    URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin"
    pin = pincode
    date = date
    cnt = 0

    for code in pin:
        params = {"pincode": code, "date": date}
        response = requests.get(URL, params)
        if response.ok:
            data = json.loads(response.text)
            # print(data)
            if data["centers"]:
                for center in data["centers"]:
                    for session in center["sessions"]:
                        if(session["min_age_limit"] < 45 and session["available_capacity"] > 0):
                            cnt += 1
                            print("\n")
                            print("Center Name: "+str(center["name"]))
                            print("Pincode: "+str(center["pincode"]))
                            print("Date: "+str(session["date"]))
                            print("Available capacity: " +
                                  str(session["available_capacity"]))
                            print("\n")
            else:
                print("No centers found")

    if cnt > 0:
        print("Slots available book as soon as possible")

    else:
        print("No slots available")


if __name__ == "__main__":
    calendarbyPIN(pin, cur_date.strftime("%d-%m-%Y"))

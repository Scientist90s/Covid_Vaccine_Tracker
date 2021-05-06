# Covid Vaccine Tracker

This repository will help people to findout the available slots for vaccination in their area. Currently, its set to show available slots for people of 18 to 45 years of age but that can be changed accordingly.

Here, one can find 2 file `tracker.py` and `tracker_with_mail.py`

## tracker.py

This file will provide you with the information on available vaccine slot in the specified pincodes.

One just need to add pincodes in the `pin` list and run the program. If the slots are available it will be shown with details like center name, pincode, date and available slots in terminal.

## tracker_with_mail.py

This will send an email with details when any of the slots are available in the specifies pincodes.

one needs to configure following paarameters for mail:

* SMTP server
* sender's mail ID
* Receiver's mail ID

After configuring all the parameters one can set to run this program in the background in their machine (PC or Laptop) and whenever some slots are available they will get notified through mail.

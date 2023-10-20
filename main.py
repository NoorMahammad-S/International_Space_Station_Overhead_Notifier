#----------------------------------ISS Overhead Notifier Project-------------------------#
import time
import requests
from datetime import datetime
import smtplib

# Your latitude and longitude
MY_LAT = 36.9981
MY_LONG = -103.5383

# Your email and password for sending notifications
NAME = "NoorMahammad-S@email.com"
PASSWORD = "xyz"


# Function to check if the International Space Station (ISS) is overhead
def is_iss_overhead():
    # Send a request to the ISS API to get its current position
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    print(data)

    # Extract the latitude and longitude of the ISS
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Check if the ISS is within +5 or -5 degrees of your position
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


# Function to check if it's currently night at your location
def is_night():
    # Send a request to get sunrise and sunset times for your location
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    # Extract sunrise and sunset times
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # Get the current time
    time_now = datetime.now().hour

    # Check if it's night by comparing the current time with sunset and sunrise times
    if time_now >= sunset or time_now <= sunrise:
        return True


             # This loop continuously checks for the conditions to send a notification
while True:
    time.sleep(60)  # Wait for 60 seconds

    # If the ISS is overhead and it's night, send an email notification
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()  # Start a secure connection
            connection.login(user=NAME, password=PASSWORD) # Log in to your email account
            connection.sendmail(
                from_addr=NAME, # Your email id
                to_addrs=NAME,  # Recipient's email id
                msg="Subject:Look Up\n\nThe ISS is above in the sky." # Email message
            )

#If the ISS is close to my current position and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



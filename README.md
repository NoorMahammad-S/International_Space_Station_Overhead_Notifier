# International_Space_Station_Overhead_Notifier

This Python script is designed to notify you when the International Space Station (ISS) is passing overhead and it's nighttime at your location. 
It does so by making use of two APIs, one to track the ISS's position and the other to determine the sunrise and sunset times at your specified coordinates.

## Features

- Monitors the ISS position and your local time to send you an email notification when the ISS is nearby and it's nighttime.
- Uses the Open Notify API to get the current ISS position.
- Utilizes the Sunrise-Sunset API to retrieve sunrise and sunset times for your location.

## Prerequisites

Before using this script, you'll need the following:

- Python 3.x installed on your system.
- Necessary Python libraries installed, which can be installed using `pip`:
  - `requests`
  - `smtplib` (for sending emails)

## Setup

1. Clone this repository to your local machine:

``` bash
git clone https://github.com/your-username/iss-overhead-notifier.git

1.Modify the script with your specific information:
  *Replace MY_LAT and MY_LONG with your latitude and longitude.
  *Replace NAME with your email address and PASSWORD with your email password for sending notifications.
2.Allow less secure apps to access your Google account if you're using Gmail. You can do this by going to your Google Account settings and enabling "Less secure apps."
3.Run the script:

''' bash
python iss_overhead_notifier.py

The script will now run continuously, checking for the ISS's position and nighttime conditions. If both conditions are met, it will send you an email notification.

# Configuration
You can modify the frequency of checks and other parameters in the script to suit your needs.

# License
This project is licensed under the MIT License. Feel free to use and modify it for your purposes.

## Note: Be cautious about storing your email password in plain text in the script. It's recommended to use environment variables or a more secure method for storing
sensitive information.

Happy stargazing!

'''css
This README provides an overview of the project, explains its features, lists prerequisites and setup instructions, and offers a brief note about security considerations. You can customize it further to add any additional details or instructions as needed for your project.

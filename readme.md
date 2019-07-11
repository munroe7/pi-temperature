# Temperature reading with POST
This project is based off the tutorial found [Here](https://www.raspberrypi-spy.co.uk/2013/03/raspberry-pi-1-wire-digital-thermometer-sensor/)

This version allows you to post your readings to a REST endpoint. Your REST endpoint can then store these readings into your database of choice.

## Getting Started

If your Pi is not formatted for English, use the following instructions on "Americanizing" your PI: [Link](http://rohankapoor.com/2012/04/americanizing-the-raspberry-pi/)

Follow the tutorial above until they have you create a python script. Instead of running their command "wget ......", run the following:
```
sudo apt-get install git
git clone git@github.com:munroe7/pi-temperature.git
sudo apt-get install python-requests
```

Before running the script you must edit read-temperature.py and change POST-URL and ROOM-NAME to your desired values

After updating the above values, run the python script by calling:
```
python pi-temperature/read-temperature.py
```

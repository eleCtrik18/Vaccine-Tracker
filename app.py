import requests
import time
from playsound import playsound
from win10toast import ToastNotifier
toast = ToastNotifier()
dist = 696  #You can have your own District Code here
date = '23-07-2021'
URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}'.format(
    dist, date)

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}


def findAvailability():
    counter = 0
    result = requests.get(URL, headers=header)
    response_json = result.json()
    data = response_json["sessions"]
    for each in data:
        if((each["available_capacity"] > 0) & (each["min_age_limit"] == 18)):
            counter = counter + 1 
            print("Vaccination Center: ",each["name"])
            print("Pincode: ",each["pincode"])
            print("State Name: ",each["state_name"])
            print("Vaccine: ",each["vaccine"])
            print("Capacity: ",each["available_capacity"])
            playsound('E:\Python\Vaccine Tracker\ding-sound.mp3')
            toast.show_toast(title = "Vaccine Availabile",msg="Book fast ",duration=10,icon_path=None)
            return True
    if(counter == 0):
        toast.show_toast(title = "No vaccine",msg="Please try again",duration=5,icon_path=None)
        print("No Slots available for now, no notification would be sent")
        
     
    


while(findAvailability() != True):
    time.sleep(5)
    findAvailability()
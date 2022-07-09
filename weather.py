import os
import requests
from geopy import Nominatim
from dotenv import load_dotenv

def get_location(city):
    geolocator = Nominatim(user_agent="myGeolocator")
    location = geolocator.geocode(city)
    return location.latitude, location.longitude


def get_weather(city):
    load_dotenv()
    apiKey = os.getenv("apiKey")
    coords = get_location(city)
    apiUrl = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude={}&units={}&appid={}".format(
        coords[0], coords[1], "hourly,minutely,alerts", "imperial", apiKey)
    res = requests.get(apiUrl).json()
    return res


def get_prep(city):
    vartest = get_weather(city)
    tmp = vartest['daily'][0]['pop']
    return tmp


def get_temp_day(city):
    vartest = get_weather(city)
    tmp0 = vartest['current']['temp']
    tmp1 = vartest['current']['weather'][0]['main']
    tmp2 = vartest['current']['weather'][0]['description']
    tmp3 = vartest['timezone']
    return tmp0, tmp1, tmp2, tmp3


def get_choices():
    print("Please select one of the below options")
    print("1- Display weather temperature and condition ")
    print("2- Display chances of rain ")
    print("3- Select a different location ")
    print("4- Exit weather service ")


def get_menu():
    loop = True

    while loop:
        print(33 * "=", "Welcome to the Weather Service", 33 * "=")
        location = input("Please type location of interest ('zip-code, country' or 'city, state' or 'city, country'): ")
        print(98 * "-")
        get_choices()
        print(98 * "=")
        choice = input("Enter your choice [1-4]: ")

        if choice == '1':
            try:
                temp = get_temp_day(location)
            except AttributeError:
                print("Type location in a different way")
                continue
            print(str('Temperature: ' + str(temp[0]) + '°F ' + '\n' +
                      'Condition: ' + str(temp[1]) + ' (' + str(temp[2]) + ')' + '\n')
                  + 'Timezone: ' + str(temp[3]))
            os.system("pause")
            os.system("cls")

        elif choice == '2':
            choice = ''
            while len(choice) == 0:
                temp = get_prep(location)
                print(str('Chance of rain: ' + str(int(temp * 100)) + '% chance of rain for the day'))
                break
            os.system("pause")
            os.system("cls")

        elif choice == '3':
            continue
            os.system("pause")

        elif choice == '4':
            print("Exiting..")
            loop = False

        else:
            input("Please enter any key to try again..")


if __name__ == "__main__":
    get_menu()

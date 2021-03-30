from datetime import datetime, timedelta
import requests

HOLIDAYURL = 'https://holidayapi.com/v1/holidays'
COUNTRY = 'CN'
LAT = '39.9042'
LON = '116.4074'
HOLIDAYKEY = 'a1b022f3-cce2-4b99-9cd3-a84b2e31f93b'
WEATHERKEY = '88b7cdc97b1b6bdbf01fa35ffe779990'
WEATHERURL = 'https://api.openweathermap.org/data/2.5/onecall'

holidayparameters={
    "country": COUNTRY,
    "year" : 2020,
    "key" : HOLIDAYKEY,
    "month" : 1,
    "day" : 1,
    "public" : False
    }

weatherparameters={
    "lat" : LAT,
    "lon" : LON,
    "exclude" : 'hourly,minutely,current,alerts',
    "appid" : WEATHERKEY
}

tod = datetime.today()
tom = tod + timedelta(days=1)
days={}
average_temp=[]

#finding average temperature for the day
response = requests.get(url=WEATHERURL, params=weatherparameters)
response.raise_for_status()
response = response.json()

temperatures = response["daily"]

#finding average temperature for the next 7 days
for i in range(7):
    x = (temperatures[i]["temp"]["min"] + temperatures[i]["temp"]["max"])/2
    average_temp.append(x)

for i in range(7):
    #input needed for the model
    date=1
    average_temperature=0
    is_weekend=True
    holiday=0
    year=1

    MONTH = tod.month
    DAY = tod.day
    YEAR = tod.year

    #finding date
    date=DAY

    #finding average temperature
    average_temperature = average_temp[i]

    #finding whether day is weekend
    if tod.weekday() == 5 or tod.weekday() == 6:
        is_weekend = True
    else:
        is_weekend = False   


    #finding whether this day is a holiday or not
    #parameters["year"] = YEAR
    holidayparameters["month"] = MONTH
    holidayparameters["day"] = DAY
    response = requests.get(url=HOLIDAYURL, params=holidayparameters )
    response.raise_for_status()
    response = response.json()
    if len(response["holidays"]):
        holiday=1
    else:
        holiday=0

    #finding year
    year = YEAR

    days[i] = {}

    days[i]["date"] = date
    days[i]["average_temperature"] = average_temperature
    days[i]["is_weekend"] = is_weekend
    days[i]["holiday"] = holiday
    days[i]["year"] = year
    tod = tod + timedelta(days=1)

print(days)
import joblib
from datetime import datetime, timedelta
import requests
import sklearn
import os
from Predictor.models import Predictions

HOLIDAYURL = 'https://holidayapi.com/v1/holidays'
COUNTRY = 'CN'
LAT = '39.9042'
LON = '116.4074'
HOLIDAYKEY = 'a1b022f3-cce2-4b99-9cd3-a84b2e31f93b'
WEATHERKEY = '88b7cdc97b1b6bdbf01fa35ffe779990'
WEATHERURL = 'https://api.openweathermap.org/data/2.5/onecall'

tod=''

def setTod():
    global tod
    tod=datetime(year=2021, month=3, day=10)

def computeForWeek():
    start_of_week = tod - timedelta(days=tod.weekday())  # Monday
    end_of_week = start_of_week + timedelta(days=6)  # Sunday
    x = start_of_week
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
    days={}
    average_temp=[]    

    #finding average temperature for the next 7 days
    response = requests.get(url=WEATHERURL, params=weatherparameters)
    response.raise_for_status()
    response = response.json()

    temperatures = response["daily"]
    for i in range(7):
        avg = (temperatures[i]["temp"]["min"] + temperatures[i]["temp"]["max"])/2
        average_temp.append(avg)

    while x<=end_of_week:
        i=x.weekday()
        #input needed for the model
        date=1
        average_temperature=0
        is_weekend=True
        holiday=0
        year=1

        MONTH = x.month
        DAY = x.day
        YEAR = x.year

        #finding date
        date=DAY

        #finding average temperature
        average_temperature = average_temp[i]

        #finding whether day is weekend
        if x.weekday() == 5 or x.weekday() == 6:
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
        x = x + timedelta(days=1)

    print(days)

    predictions = loadModel(days)
    print(predictions)
    addToDB(predictions)

def loadModel(days):
    predictions=[]
    cls = joblib.load('final.sav')

    for i in range(7):
        x = cls.predict([[days[i]["year"], days[i]["date"], days[i]["holiday"], days[i]["is_weekend"], days[i]["average_temperature"]]])
        predictions.append(x.tolist()[0])
    return predictions

def addToDB(predictions):
    start_of_week = tod - timedelta(days=tod.weekday())  # Monday
    end_of_week = start_of_week + timedelta(days=6)  # Sunday
    y = start_of_week
    while y<=end_of_week:
        i = y.weekday()
        x = Predictions(date = y.strftime('%d/%m/%Y'), day=y.strftime("%A"), prediction=predictions[i])        
        x.save()
        y = y + timedelta(days=1) 

def readFromDB():
    start_of_week = tod - timedelta(days=tod.weekday())  # Monday
    end_of_week = start_of_week + timedelta(days=6)  # Sunday
    y=start_of_week
    result={}

    while y<=end_of_week:
        date = y.strftime('%d/%m/%Y')
        i=y.weekday()
        result[i]={}
        x = Predictions.objects.get(pk=date)
        result[i]["date"] = x.date
        result[i]["day"] = x.day
        result[i]["prediction"] = x.prediction

        y = y + timedelta(days=1)

    return result        

def isNewUser():
    queryset = Predictions.objects.filter(date=tod.strftime('%d/%m/%Y'))
    return not queryset.exists()

def computePredictions():
    result={}
    if tod.weekday() == 0 or isNewUser():
        computeForWeek()
        result=readFromDB()

    else:
        result=readFromDB()
    return result

def getNameOfToday():
    return tod.strftime("%A")

def getDateOfToday():
    return tod.strftime('%d/%m/%Y')

def getPredictionOfToday():
    date = tod.strftime('%d/%m/%Y')
    x =  Predictions.objects.get(pk=date)
    return x.prediction


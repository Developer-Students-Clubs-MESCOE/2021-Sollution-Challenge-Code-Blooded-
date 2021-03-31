from django.shortcuts import render
import joblib
from datetime import datetime, timedelta
from . import compute

HOLIDAYURL = 'https://holidayapi.com/v1/holidays'
COUNTRY = 'CN'
LAT = '39.9042'
LON = '116.4074'
HOLIDAYKEY = 'a1b022f3-cce2-4b99-9cd3-a84b2e31f93b'
WEATHERKEY = '88b7cdc97b1b6bdbf01fa35ffe779990'
WEATHERURL = 'https://api.openweathermap.org/data/2.5/onecall'


# Create your views here.
def showResult(request):
    result=compute.computePredictions()
    todayDate = compute.getDateOfToday()
    todayName = compute.getNameOfToday()
    todayPrediction = compute.getPredictionOfToday()
    # print(result)
    # print(todayDate)
    # print(todayName)
    # print(todayPrediction)
    return render(request, "predictor\\result.html", 
    {
        "result" : result,
        "todayDate" : todayDate,
        "todayName" : todayName,
        "todayPrediction" : todayPrediction
    })
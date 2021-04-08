from django.shortcuts import render
import joblib
from .compute import *
from .inventory import *

# Create your views here.
def showResult(request):
    setTod()
    result=computePredictions()
    todayDate =getDateOfToday()
    todayName = getNameOfToday()
    todayPrediction = getPredictionOfToday()
    startOfWeek = getStartOfWeek()
    endOfWeek = getEndOfWeek()
    total = getTotalOfWeek()

    # print(result)
    # print(todayDate)
    # print(todayName)
    # print(todayPrediction)
    return render(request, "predictor\\result.html", 
    {
        "result" : result,
        "todayDate" : todayDate,
        "todayName" : todayName,
        "todayPrediction" : todayPrediction, 
        "startOfWeek" : startOfWeek,
        "endOfWeek" : endOfWeek,
        "total" : total
    })
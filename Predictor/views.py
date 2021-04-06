from django.shortcuts import render
import joblib
from .compute import *

# Create your views here.
def showResult(request):
    setTod()
    result=computePredictions()
    todayDate =getDateOfToday()
    todayName = getNameOfToday()
    todayPrediction = getPredictionOfToday()
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
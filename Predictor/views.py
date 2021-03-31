from django.shortcuts import render
import joblib
from datetime import datetime, timedelta
from . import compute

# Create your views here.
def showResult(request):
    compute.setTod()
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
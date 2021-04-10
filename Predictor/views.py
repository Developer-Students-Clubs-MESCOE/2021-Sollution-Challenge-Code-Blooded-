from django.shortcuts import render
import joblib
from .compute import *
from .inventory import *
from django.conf import settings

# Create your views here.
def showResult(request):
    setTod()
    result = computePredictions() #dictionary that contains Predictions for the entire week
    # format= {weekday : {"date": , "day": , "prediction": }}

    todayDate = getDateOfToday()
    todayName = getNameOfToday()
    todayWeekday = getWeekdayOfToday()

    todayPrediction = getPredictionOfToday() #integer that has predictions for the current day only

    startOfWeek = getStartOfWeek()
    endOfWeek = getEndOfWeek()

    total = getTotalOfWeek()

    todayOrders = temp(todayPrediction) #dictionary that contains breakdown of the orders of the current day
    #format= {i : {"name": , "quantity": }}
    weekOrders = temp(total) #dictionary that contains breakdown of the orders of the week
    #format= {i : {"name": , "quantity": }}

    # print(todayOrders)
    # print(weekOrders)

    todayInventory = getInventory(todayOrders) #this dictionary only has inventory for the current day
    weeklyInventory = getInventory(weekOrders) #this dictionary has the sum total for the week
    #format= {ingredientID : {"name": , "quantity": (decimal), "unit": , "display" : (str)}}

    # print(todayInventory)
    # print(weeklyInventory)
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
        "total" : total, 
        "todayOrders" : todayOrders,
        "weeklyOrders" : weekOrders,
        "todayInventory" : todayInventory,
        "weeklyInventory" : weeklyInventory
    })

def resultTemplate(request):
    return render(request,"predictor\\index.html",
    {
    'default_domain': settings.DEFAULT_DOMAIN
    }
    )
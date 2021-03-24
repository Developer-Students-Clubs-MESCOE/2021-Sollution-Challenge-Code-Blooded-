from django.shortcuts import render
import joblib
import datetime

# Create your views here.

def showResult(request):
    cls = joblib.load('finalized_model.sav')
    x = cls.predict([[2013, 5, 1, 0]])
    result = x.tolist()[0]
    return render(request, "predictor\\result.html", 
    {
        "result" : round(result)
    })
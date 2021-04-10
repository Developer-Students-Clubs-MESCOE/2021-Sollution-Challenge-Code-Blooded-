from django.urls import path

from .views import showResult, resultTemplate

urlpatterns=[
    path("", showResult, name="result" ), 
    path("new", resultTemplate, name="newresult"),   
]

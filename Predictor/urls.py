from django.urls import path

from .views import showResult

urlpatterns=[
    path("", showResult, name="result" )
]

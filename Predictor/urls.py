from django.urls import path

from . import views

urlpatterns=[
    path("", views.showResult, name="result" )
]

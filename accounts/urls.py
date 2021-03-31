from django.urls import path
from .views import UserRegisterView

urlpatterns = [

    path('signup/' , UserRegisterView.as_view(), name = 'signup'),    

    

]
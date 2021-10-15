from django.urls import path, include
from .import views

urlpatterns = [
    path('winequality/',views.winequality,name='winequality'),
    path('result/',views.result,name='result'),
]
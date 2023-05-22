from django.urls import path
from .Views import *

urlpatterns = [
    path('listEvent', getEvents, name="getEvents"),
]

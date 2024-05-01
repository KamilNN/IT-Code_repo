from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

current_datetime = datetime.now()

def index(request):
    return HttpResponse(current_datetime)

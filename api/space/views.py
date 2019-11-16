from django.shortcuts import render
from requests import get
import json
from django.http import HttpResponse

def past_capsules(request):
    r = get('https://api.spacexdata.com/v3/capsules/past')
    return HttpResponse(r.json())

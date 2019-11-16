from django.shortcuts import render
from requests import get
import json
from django.http import HttpResponse

def past_capsules(request):
    r = get('https://api.spacexdata.com/v3/capsules/past')
    return HttpResponse(r.json())


def upcoming_capsules(request):
    r = get('https://api.spacexdata.com/v3/capsules/upcoming')
    return HttpResponse(r.json())


def all_capsules(request):
    r = get('https://api.spacexdata.com/v3/capsules')
    return HttpResponse(r.json())


def past_capsule(request):
    r = get('https://api.spacexdata.com/v3/capsules/past')
    past_capsules = r.json()
    serial = past_capsules[-1]['capsule_serial']
    past_capsule = get('https://api.spacexdata.com/v3/capsules/{}'.format(serial))
    return HttpResponse(past_capsule)

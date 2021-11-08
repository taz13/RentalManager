from django.http import HttpResponse
from django.shortcuts import render
import requests

# Create your views here.
def index(request):


    url = "https://zillow-com1.p.rapidapi.com/propertyExtendedSearch"

    querystring = {"location": "Ontario", "status_type": "ForSale", "home_type": "Houses, Townhomes"}

    headers = {
        'x-rapidapi-host': "zillow-com1.p.rapidapi.com",
        'x-rapidapi-key': "be7b441027msh62351d6edecc63ap1c97a2jsnc5e03c8e0fe0"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return HttpResponse(response.text)

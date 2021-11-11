from django.http import HttpResponse
import requests

from RentalManager.ConfigManager import ConfigManager
from RentalManager.firebase import Firebase


firebaseDb = Firebase()

def index(request):
    provinceArray = ["Ontario", "Quebec", "New Brunswick", "Nova Scotia", "Newfoundland and Labrador", "British Columbia",
                     "Alberta", "Manitoba", "Prince Edward Island", "Saskatchewan"]

    configManager = ConfigManager('ApiConfig.properties')
    for province in provinceArray:
       url = configManager.getPropertyValue('ApiSection', 'api.url')

       querystring = {"location": province, "status_type": "ForSale", "home_type": "Houses, Townhomes"}

       headers = {
           'x-rapidapi-host': configManager.getPropertyValue('ApiSection', 'api.host'),
           'x-rapidapi-key': configManager.getPropertyValue('ApiSection', 'api.key')
       }

       response = requests.request("GET", url, headers=headers, params=querystring)

       propertiesJson = response.json()

       firebaseDb.savePropertiesToDb(propertiesJson,province)

    return HttpResponse("Success")

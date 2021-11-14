from django.http import HttpResponse, Http404
from django.shortcuts import render

from RentalManager.firebase import Firebase
from rentEstimator.apiUtil import ZillowApi

firebaseDb = Firebase()

def getPropertyData(request):
    provinceArray = ["Ontario", "Quebec", "New Brunswick", "Nova Scotia", "Newfoundland and Labrador", "British Columbia",
                     "Alberta", "Manitoba", "Prince Edward Island", "Saskatchewan"]
    for province in provinceArray:
       zillowApi = ZillowApi()
       propertiesList = zillowApi.getPropertyList(province)
       firebaseDb.savePropertiesToDb(propertiesList, province)

    return HttpResponse("Success")

def getRentEstimate(request,province):
    try:
        propertiesList = firebaseDb.getPropertiesData(province)
    except Exception as e:
        raise Http404("Error getting property data!!!")
    return render(request, 'rentEstimator/index.html', {'property_list' : propertiesList})

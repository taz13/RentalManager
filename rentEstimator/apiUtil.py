import time

import requests
from RentalManager.ConfigManager import ConfigManager


class ZillowApi:
    def __init__(self):
        self.configManager = ConfigManager('ApiConfig.properties')


    def getPropertiesPerPage(self,province,pageNumber):
        url = self.configManager.getPropertyValue('PropertyApiSection', 'api.url')

        querystring = {"location": province, "status_type": "ForSale", "page": pageNumber,
                       "home_type": "Houses, Townhomes, Condos, Apartments"}

        headers = {
            'x-rapidapi-host': self.configManager.getPropertyValue('PropertyApiSection', 'api.host'),
            'x-rapidapi-key': self.configManager.getPropertyValue('PropertyApiSection', 'api.key')
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        return response.json()

    def getPropertyList(self,province):
        propertyList = []

        propertiesJson = self.getPropertiesPerPage(province,0)
        propertyList = propertyList + propertiesJson['props']
        pages=propertiesJson['totalPages']+1
        time.sleep(1)

        if pages>2:
            for x in range(1,pages):
                propertiesJson = self.getPropertiesPerPage(province, x)
                propertyList = propertyList + propertiesJson['props']
                time.sleep(1)
        return propertyList

    def getRentEstimate(self,propertyInfo):
        url = self.configManager.getPropertyValue('RentEstimateApiSection', 'rentEstimateApi.url')

        propertyType = {
            "SingleFamily": "SINGLE_FAMILY",
            "Condo": "CONDO",
            "MultiFamily": "MULTI_FAMILY",
            "Townhouse": "TOWNHOUSE"
        }
        querystring = {"propertyType": propertyType[propertyInfo.propertyType], "address": propertyInfo.address,
                       "long": propertyInfo.longitude, "lat": propertyInfo.latitude, "beds": propertyInfo.bedrooms,
                       "baths": propertyInfo.bathrooms, "sqftMin": propertyInfo.livingArea}

        headers = {
            'x-rapidapi-host': self.configManager.getPropertyValue('RentEstimateApiSection', 'rentEstimateApi.host'),
            'x-rapidapi-key': self.configManager.getPropertyValue('RentEstimateApiSection', 'rentEstimateApi.key')
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        return response.json()
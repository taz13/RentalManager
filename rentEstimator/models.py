from rentEstimator import mortgage


class PropertyInfo:
    def __init__(self, propertyObj):
        m = mortgage.Mortgage(interest=0.0175, amount=propertyObj['price'], months=360)
        mapUrlFormat= "https://www.google.ca/maps/@{lat:.5f},{long:.5f},16.33z"
        if propertyObj['latitude'] is None or propertyObj['longitude'] is None:
            mapUrl = ""
        else:
            mapUrl = mapUrlFormat.format(lat=propertyObj['latitude'], long=propertyObj['longitude'])
        self.propertyInfoDict= {'zpId': propertyObj['zpid'], 'address': propertyObj['address'],
                                'country': propertyObj['country'], 'currency': propertyObj['currency'],
                                'imgSrc': propertyObj['imgSrc'], 'latitude': propertyObj['latitude'],
                                'longitude': propertyObj['longitude'], 'price': propertyObj['price'],
                                'propertyType': propertyObj['propertyType'],
                                'city': propertyObj['address'].split(",")[1].strip(), 'minRent': propertyObj['price'] * 0.0075,
                                'monthlyMortgage': m.monthly_payment(), 'mapUrl':mapUrl}




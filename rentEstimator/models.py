

class PropertyInfo:
    def __init__(self, propertyObj):
        self.propertyInfoDict= {'zpId': propertyObj['zpid'], 'address': propertyObj['address'],
                                'country': propertyObj['country'], 'currency': propertyObj['currency'],
                                'imgSrc': propertyObj['imgSrc'], 'latitude': propertyObj['latitude'],
                                'longitude': propertyObj['longitude'], 'price': propertyObj['price'],
                                'propertyType': propertyObj['propertyType'],
                                'city': propertyObj['address'].split(",")[1], 'minRent': propertyObj['price'] * 0.0075}




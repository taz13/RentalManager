import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from rentEstimator.models import PropertyInfo


class Firebase:

    def __init__(self):
        cred = credentials.Certificate('rental-manager-firebase-credential.json')
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def savePropertiesToDb(self,propertiesArray,province):
        for index,propertyData in enumerate(propertiesArray):
            propertyTitle = "Properties #" + str(index)
            property = PropertyInfo(propertyData)
            doc_ref = self.db.collection(province).document(propertyTitle)
            doc_ref.set(property.propertyInfoDict)

    def getPropertiesData(self,location):
        if "-" in location:
            locationParams=location.split("-")
            docs = self.db.collection(locationParams[1]).where(u'city', u'==', locationParams[0]).stream()
        else:
            docs = self.db.collection(location).order_by(u'price').stream()

        propertyList = []
        if docs is None:
            return u'No such document!'
        else:
            for doc in docs:
                propertyList.append(doc.to_dict())
            return propertyList
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class Firebase:

    def __init__(self):
        cred = credentials.Certificate('rental-manager-firebase-credential.json')
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def savePropertiesToDb(self,propertiesJson,province):
        propertiesArray = propertiesJson['props']

        for index,property in enumerate(propertiesArray):
            propertyTitle = "Properties #" + str(index)
            doc_ref = self.db.collection(province).document(propertyTitle)
            doc_ref.set(property)

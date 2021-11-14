# RentalManager
Python application for Rental Management

This a python web application built on Django framework. This application will have different features to help manage rental properties.

**Environment Setup**

[For MAC only]
Run "setup.sh" and it will install homebrew,python,pip and django.

This application connects to a firebase database. Please setup firebase db and firebase admin.
Setup firebase with Django: https://medium.com/@canadiyaman/how-to-use-firebase-with-django-project-34578516bafe

Also go to Rapid API(https://rapidapi.com/apimaker/api/zillow-com1/) to get the API key

To run the application run the following command in terminal:

"python3 manage.py runserver"

Example of API end point:

1. Get all properties for a province: http://127.0.0.1:8000/rentalManager/rentEstimate/Ontario
2. Get all properties for a city: http://127.0.0.1:8000/rentalManager/rentEstimate/Saint%20Patrick's%20Parish-Prince%20Edward%20Island
3. Update db with latest property info: http://127.0.0.1:8000/rentalManager/GetPropertyData

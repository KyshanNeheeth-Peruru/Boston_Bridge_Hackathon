from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, get_user_model, authenticate
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from .models import Event, Violation
import requests
import csv
from django import forms
from io import TextIOWrapper
from django.http import HttpResponse
from django.conf import settings
import googlemaps
import joblib
import os
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Create your views here.

def home(request):
    events = Event.objects.all()
    return render(request, 'home.html', {'events': events})

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Logged In.')
            return redirect('home')

        else:
            messages.error(request, "Username or password invalid")
            return redirect('login')
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        username= request.POST['username']
        firstname= request.POST['firstname']
        lastname= request.POST['lastname']
        email= request.POST['email']
        pasw1= request.POST['pasw1']
        pasw2= request.POST['pasw2']
        user = User.objects.create_user(username,email,pasw1)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        messages.success(request, 'User created.')
        return render(request, 'home.html')
    return render(request, 'register.html')

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            messages.success(request, 'Password recovery email sent.')
        else:
            messages.error(request, 'No user found with this email.')
    return render(request, 'forgot_password.html')

def logout_view(request):
    logout(request)
    messages.success(request,"Logged out")
    return redirect('home')

class CSVUploadForm(forms.Form):
    file = forms.FileField()

def add_rc(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = TextIOWrapper(request.FILES['file'].file, encoding='utf-8')
            reader = csv.DictReader(csv_file)
            for row in reader:
                Violation.objects.create(
                    violation_type=row['violation_type'],
                    description=row['description'],
                    address=row['address'],
                )
            messages.success(request, "CSV file has been successfully uploaded and processed.")
            return redirect('add_rc')
    else:
        form = CSVUploadForm()
    
    return render(request, 'add_rc.html', {'form': form})


def navigation(request):
    if request.method == 'POST':
        source = request.POST['source']
        destination = request.POST['destination']
        mode = request.POST['mode']
        api_key = 'AIzaSyDSRumQMKR9GclqYS9AlfwlTRd1pUpcWRk'
        base_url = "https://maps.googleapis.com/maps/api/directions/json"
        params = {
            "key": api_key,
            "origin": source,
            "destination": destination,
            "mode": mode
        }
        response = requests.get(base_url, params=params)
        directions = response.json()
        route = directions["routes"][0]
        legs = route["legs"][0]
        duration = legs["duration"]["text"]
        distance = legs["distance"]["text"]
        steps = legs["steps"]

        print(duration)
        print(distance)

        return render(request, 'navigation.html', {'route': route, 'distance': distance,'duration': duration, 'steps': steps})
        
    return render(request, 'navigation.html')

def rental_check(request):
    violations = []
    if request.method == 'POST':
        address = request.POST.get('address', '') 
        violations = Violation.objects.filter(address__icontains=address)
    return render(request, 'rental_check.html', {'violations': violations})

def nearby_events(request):
    places = []
    if request.method == 'POST':
        api_key = 'AIzaSyDSRumQMKR9GclqYS9AlfwlTRd1pUpcWRk'
        keyword = request.POST.get('activity', '')
        address = request.POST.get('address', '')
        location = geocode_address(api_key, address)
        radius = "5000"
        places = find_places_nearby(api_key, location, radius, keyword=keyword)
        return render(request, 'nearby_events.html', {'places': places, 'address':address})
    return render(request, 'nearby_events.html', {'places': places})

def geocode_address(api_key, address):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "key": api_key,
        "address": address
    }
    response = requests.get(base_url, params=params)
    result = response.json()["results"][0]
    location = result["geometry"]["location"]
    return f"{location['lat']},{location['lng']}"

def find_places_nearby(api_key, location, radius, keyword=None, type=None):
    base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "key": api_key,
        "location": location,
        "radius": radius
    }
    if keyword:
        params["keyword"] = keyword
    if type:
        params["type"] = type

    response = requests.get(base_url, params=params)
    results = response.json()["results"]
    return results

def rent_predict(request):
    gmaps = googlemaps.Client(key='AIzaSyDSRumQMKR9GclqYS9AlfwlTRd1pUpcWRk')

    if request.method == 'POST':
        model_path = os.path.join(settings.BASE_DIR, 'ml_models', 'rent_price.joblib')
        rf = joblib.load(model_path)
        address = request.POST['address']
        rooms = request.POST['rooms']
        baths = request.POST['baths']
        typeofhouse = request.POST['typeofhouse']
        geocode_result = gmaps.geocode(address)
        
        if geocode_result:
            latitude = geocode_result[0]['geometry']['location']['lat']
            longitude = geocode_result[0]['geometry']['location']['lng']
    
            for component in geocode_result[0]['address_components']:
                if 'postal_code' in component['types']:
                    zipcode = component['long_name']
                    break
            prediction=rf.predict(np.array([zipcode,latitude,longitude,typeofhouse,baths,rooms]).reshape(1, -1))
            print(prediction)
            print(f"Latitude: {latitude}, Longitude: {longitude}, ZIP Code: {zipcode}")
            return render(request, 'rent_predict.html', {'prediction': prediction, })
        else:
            print("No results found.")
        
    return render(request, 'rent_predict.html')

def student_discounts(request):
    return render(request, 'student_discounts.html')


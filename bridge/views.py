from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, get_user_model, authenticate
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from .models import Event
import requests

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

def faq(request):
    return render(request, 'faq.html')

def add_rc(request):
    return render(request, 'add_rc.html')


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

def urban_commuter(request):
    return render(request, 'urban_commuter.html')

def local_community_engagement(request):
    return render(request, 'local_community_engagement.html')

def student_housing(request):
    return render(request, 'student_housing.html')

def job_finder(request):
    return render(request, 'job_finder.html')

def event_planning_tools(request):
    return render(request, 'event_planning_tools.html')

def campus_to_city_transition(request):
    return render(request, 'campus_to_city_transition.html')

def student_discounts(request):
    return render(request, 'student_discounts.html')

def emergency_response(request):
    return render(request, 'emergency_response.html')

def networking(request):
    return render(request, 'networking.html')

def culture_exchange_platforms(request):
    return render(request, 'culture_exchange_platforms.html')

def health_portal(request):
    return render(request, 'health_portal.html')

def green_campus(request):
    return render(request, 'green_campus.html')

def educational_partnerships(request):
    return render(request, 'educational_partnerships.html')

def ciy_exploration(request):
    return render(request, 'ciy_exploration.html')

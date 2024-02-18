from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def forgot_password(request):
    return render(request, 'forgot_password.html')

def faq(request):
    return render(request, 'faq.html')

def urban_commuter(request):
    return render(request, 'urban_commuter.html')

def city_Navigation(request):
    return render(request, 'city_Navigation.html')

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

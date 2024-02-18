"""
URL configuration for bostonbridge project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bridge import views as bridge_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bridge_views.home, name='home'),
    path('login/', bridge_views.login, name='login'),
    path('register/', bridge_views.register, name='register'),
    path('forgot_password/', bridge_views.forgot_password, name='forgot_password'),
    path('faq/', bridge_views.faq, name='faq'),
    
    path('urban_commuter/', bridge_views.urban_commuter, name='urban_commuter'),
    path('city_Navigation/', bridge_views.city_Navigation, name='city_Navigation'),
    path('local_community_engagement/', bridge_views.local_community_engagement, name='local_community_engagement'),
    path('student_housing/', bridge_views.student_housing, name='student_housing'),
    path('job_finder/', bridge_views.job_finder, name='job_finder'),
    path('event_planning_tools/', bridge_views.event_planning_tools, name='event_planning_tools'),
    path('campus_to_city_transition/', bridge_views.campus_to_city_transition, name='campus_to_city_transition'),
    path('student_discounts/', bridge_views.student_discounts, name='student_discounts'),
    path('emergency_response/', bridge_views.emergency_response, name='emergency_response'),
    path('networking/', bridge_views.networking, name='networking'),
    path('culture_exchange_platforms/', bridge_views.culture_exchange_platforms, name='culture_exchange_platforms'),
    path('health_portal/', bridge_views.health_portal, name='health_portal'),
    path('green_campus/', bridge_views.green_campus, name='green_campus'),
    path('educational_partnerships/', bridge_views.educational_partnerships, name='educational_partnerships'),
    path('ciy_exploration/', bridge_views.ciy_exploration, name='ciy_exploration'),

]

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contact/',views.contact,name="contact"),
    # path('info/',views.info,name="info"),
    # path('experience',views.experience,name="experience"),
]
from django.urls import path
from . import views

app_name = 'workstamp'

urlpatterns = [
    path('home/', views.home_view, name='home'),  # Home page
    path('punch_in/', views.punch_in_view, name='punch_in'),  # Punch In
    path('punch_out/', views.punch_out_view, name='punch_out'),  # Punch Out
]
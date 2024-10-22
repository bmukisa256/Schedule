from django.urls import path, include
from .views import register, login_view, logout

urlpatterns = [
    path('', login_view, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
]
from django.urls import path, include
from .views import register, login_view, logout

urlpatterns = [
    path('register/', register, name='register'),
    path('', login_view, name='login'),
    path('logout/', logout, name='logout'),
]
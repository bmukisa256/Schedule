from django.urls import path
from .views import log_time, home_view, create_workstamp

app_name = 'workstamp'

urlpatterns = [
    path('', home_view, name='home'),  # Home view
    path('log_time/', log_time, name='log_time'), # Log time view
    #path('workstamp/', log_time, name='log_time'),  
    path('create/', create_workstamp, name='create_workstamp'),  # Create workstamp view
]
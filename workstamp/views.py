from django.shortcuts import render, redirect
from .models import Workstamp
from django.utils import timezone
from django.contrib.auth.decorators import login_required
import logging

# Set up logging
logger = logging.getLogger(__name__)

@login_required
def home_view(request):
    # Fetch log time details
    log_time_details = get_user_log_time(request.user)

    # Render the home view with a welcome message and log time details
    context = {
        'welcome_message': 'Welcome to the Workstamp application!',
        'user': request.user,
        'log_time_details': log_time_details,
    }
    return render(request, 'workstamp/home.html', context)

# Function returns the log time details for the user
def get_user_log_time(user):
    return Workstamp.objects.filter(employee=user).order_by('-punch_in_time')

@login_required
def log_time(request):
    context = {}

    if request.method == 'POST':
        try:
            if 'punch_in' in request.POST:
                create_workstamp(request.user)
            elif 'punch_out' in request.POST:
                update_workstamp(request.user, 'punch_out')
            elif 'activity' in request.POST:
                update_workstamp(request.user, 'activity', request.POST.get('activity', ''))
            return redirect('workstamp:home')  # Redirect after processing the request
        except Exception as e:
            logger.error(f"Error in log_time view: {e}")
            context['error_message'] = "An error occurred while logging time. Please try again."

    # Fetch log time details to show on the log time page
    context['log_time_details'] = get_user_log_time(request.user)
    return render(request, 'workstamp/log_time.html', context)

def create_workstamp(user):
    if user is None:
        logger.error("Error: User cannot be None.")
        return

    try:
        # Check if a workstamp already exists for today
        existing_workstamp = Workstamp.objects.filter(employee=user, punch_in_time__date=timezone.now().date()).first()
        if existing_workstamp:
            logger.warning("Workstamp for today already exists. Cannot create a new one.")
            return "Workstamp for today already exists. Cannot create a new one." 

        Workstamp.objects.create(employee=user, punch_in_time=timezone.now())
        logger.info("Workstamp created successfully.")
    except Exception as e:
        logger.error(f"Error creating workstamp: {e}")
        return "Error creating workstamp."

def update_workstamp(user, update_type, activity=None):
    try:
        workstamp = Workstamp.objects.get(employee=user, punch_in_time__date=timezone.now().date())
        
        if update_type == 'punch_out':
            workstamp.punch_out_time = timezone.now()
        elif update_type == 'activity' and activity:
            if workstamp.activities:
                workstamp.activities += f'\n{activity}'
            else:
                workstamp.activities = activity
        
        workstamp.save()
        logger.info("Workstamp updated successfully.")
    except Workstamp.DoesNotExist:
        logger.error("No workstamp found for today.")
    except Exception as e:
        logger.error(f"Error updating workstamp: {e}")

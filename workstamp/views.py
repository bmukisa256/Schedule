from django.shortcuts import render, redirect
from .models import Workstamp
from django.utils import timezone

def home_view(request):
    user = request.user
    today_log = Workstamp.objects.filter(user=user, date=timezone.now().date()).first()

    if today_log and today_log.is_punched_in():
        button_text = "Punch Out"
        punch_out_url = 'punch_out'
    else:
        button_text = "Log Your Time"
        punch_in_url = 'punch_in'
    
    return render(request, 'workstamp/home.html', {
        'button_text': button_text,
        'punch_out_url': punch_out_url if today_log and today_log.is_punched_in() else None,
        'punch_in_url': punch_in_url if not today_log or not today_log.is_punched_in() else None
    })

# Punch In
def punch_in_view(request):
    user = request.user
    today_log, created = Workstamp.objects.get_or_create(user=user, date=timezone.now().date())
    
    if today_log.punch_in_time is None:  # If not punched in yet
        today_log.punch_in_time = timezone.now()
        today_log.save()
    
    return redirect('workstamp:home')  # Redirect to home page after punching in

# Punch Out and Log Activities
def punch_out_view(request):
    user = request.user
    today_log = Workstamp.objects.filter(user=user, date=timezone.now().date()).first()
    
    if request.method == "POST":
        activities = request.POST.get('activities')
        today_log.activities = activities
        today_log.punch_out_time = timezone.now()
        today_log.save()
        return redirect('workstamp:home')
    
    return render(request, 'punch_out.html', {'log': today_log})

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Workstamp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    punch_in_time = models.DateTimeField(null=True, blank=True)
    punch_out_time = models.DateTimeField(null=True, blank=True)
    activities = models.TextField(null=True, blank=True)
    date = models.DateField(default=timezone.now)

    def is_punched_in(self):
        return self.punch_in_time is not None and self.punch_out_time is None


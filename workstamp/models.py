from django.db import models
from django.contrib.auth.models import User

class Workstamp(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    punch_in_time =  models.DateTimeField(null=True, blank=True)
    punch_out_time =  models.DateTimeField(null=True, blank=True)
    activities = models.TextField(blank=True)


    def __str__(self):
        return f'{self.employee.username} - {self.date}'



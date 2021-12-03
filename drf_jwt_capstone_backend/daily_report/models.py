from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()

# Create your models here.


class DailyReport(models.Model):
    report_id = models.IntegerField.primary_key=True
    officer_id = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=False)
    calls_for_service = models.IntegerField( blank=True, default=0)
    reports = models.IntegerField(blank=True, default=0)
    supplements = models.IntegerField(blank=True, default=0)
    citations_issued = models.IntegerField(blank=True, default=0)
    warnings_issued = models.IntegerField(blank=True, default=0)
    traffic_stops = models.IntegerField(blank=True, default=0)
    citizen_contacts = models.IntegerField(blank=True, default=0)
    juvenile_contacts = models.IntegerField(blank=True, default=0)
    assigned_area = models.CharField(max_length=30, blank=True)
    assigned_vehicle = models.IntegerField(blank=True, default=0)
    miles_driven = models.IntegerField(blank=True, default=0)
    hours_worked = models.IntegerField(blank=True, default=0)
    case_numbers = models.CharField(max_length=200, blank=True)

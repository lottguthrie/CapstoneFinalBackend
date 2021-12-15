
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


# Create your models here.

# To add new columns to the authentication_user table include the properties
# in the model below
# In order for the new columns to appear in the database run:
# 1. python manage.py makemigrations
# 2. python manage.py migrate


class User(AbstractUser):
    middle_name = models.CharField(max_length=20)
    phone_number = models.IntegerField(blank=True, null= True, default=0)
    badge_number = models.IntegerField(blank=True, null= True, default=0)
    officer_id = models.IntegerField(blank=True, null= True, default=0)
    supervisor_id = models.IntegerField(blank=True, null= True, default=0)

    def __str__(self):
        return self.get_full_name


user = get_user_model()

class DailyReport(models.Model):
    report_id = models.IntegerField(blank=True, null= True, default=0)
    officer_id = models.IntegerField(blank=True, null= True, default=0)
    date = models.DateTimeField(auto_now_add=False)
    calls_for_service = models.IntegerField(blank=True, null= True, default=0)
    reports = models.IntegerField(blank=True, null= True, default=0)
    supplements = models.IntegerField(blank=True, null= True, default=0)
    citations_issued = models.IntegerField(blank=True, null= True, default=0)
    warnings_issued = models.IntegerField(blank=True, null= True, default=0)
    traffic_stops = models.IntegerField(blank=True, null= True, default=0)
    citizen_contacts = models.IntegerField(blank=True, null= True, default=0)
    juvenile_contacts = models.IntegerField(blank=True, null= True, default=0)
    assigned_area = models.CharField(max_length=20, blank=True, null= True)
    assigned_vehicle = models.IntegerField(blank=True, null= True, default=0)
    miles_driven = models.IntegerField(blank=True, null= True, default=0)
    hours_worked = models.IntegerField(blank=True, null= True, default=0)
    case_numbers = models.CharField(max_length=20, blank=True, null= True)

    def __str__(self):
        return self.report_id

class Supervisor(AbstractUser):
    supervisor_id = models.IntegerField(blank=True, null= True, default=0)
    officer_id = models.IntegerField(blank=True, null= True, default=0)
    last_name = models.CharField(max_length=20, blank=True, null= True)
    first_name = models.CharField(max_length=20, blank=True, null= True)
    middle_name = models.CharField(max_length=20, blank=True, null= True)
    badge_number = models.IntegerField(blank=True, null= True, default=0)

    def __str__(self):
        return self.supervisor_id
    
class SupervisorReport(models.Model):
    supervisor_report_id = models.IntegerField(blank=True, null= True, default=0)
    supervisor_id = models.IntegerField(blank=True, null= True, default=0)
    date = models.DateTimeField(auto_now_add=False)
    total_calls_for_service = models.IntegerField(blank=True, null= True, default=0)
    total_case_numbers_pulled = models.IntegerField(blank=True, null= True, default=0)
    total_case_numbers_completed = models.IntegerField(blank=True, null= True, default=0)
    total_reports = models.IntegerField(blank=True, null= True, default=0)
    total_supplements = models.IntegerField(blank=True, null= True, default=0)
    total_vehicles_assigned = models.IntegerField(blank=True, null= True, default=0)
    total_miles_driven = models.IntegerField(blank=True, null= True, default=0)
    officers_on_road = models.IntegerField(blank=True, null= True, default=0)
    officers_on_desk = models.IntegerField(blank=True, null= True, default=0)
    officers_on_jail_duty = models.IntegerField(blank=True, null= True, default=0)
    officers_on_light_duty = models.IntegerField(blank=True, null= True, default=0)
    officers_out_sick = models.IntegerField(blank=True, null= True, default=0)
    officers_in_training = models.IntegerField(blank=True, null= True, default=0)
    officers_on_vacation = models.IntegerField(blank=True, null= True, default=0)
    officers_assigned_elswhere = models.IntegerField(blank=True, null= True, default=0)
    total_citations_issued = models.IntegerField(blank=True, null= True, default=0)
    total_warnings_issued = models.IntegerField(blank=True, null= True, default=0)
    total_citizen_contacts = models.IntegerField(blank=True, null= True, default=0)
    total_traffic_stops = models.IntegerField(blank=True, null= True, default=0)
    total_arrest_made = models.IntegerField(blank=True, null= True, default=0)
    total_juvenile_contacts = models.IntegerField(blank=True, null= True, default=0)

    def __str__(self):
        return self.supervisor_report_id
from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()


# Create your models here.

# Create your models here.
class SupervisorReport(models.Model):
    supervisor_report_id = models.IntegerField(blank=True, primary_key=True, default=0)
    supervisor_id = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    date = models.DateTimeField
    total_calls_for_service = models.IntegerField(blank=True, default=0)
    total_case_numbers_pulled = models.IntegerField(blank=True, default=0)
    total_case_numbers_completed = models.IntegerField(blank=True, default=0)
    total_reports = models.IntegerField(blank=True, default=0)
    total_supplements = models.IntegerField(blank=True, default=0)
    total_vehicles_assigned = models.IntegerField(blank=True, default=0)
    total_miles_driven = models.IntegerField(blank=True, default=0)
    officers_on_road = models.IntegerField(blank=True, default=0)
    officers_on_desk = models.IntegerField(blank=True, default=0)
    officers_on_jail_duty = models.IntegerField(blank=True, default=0)
    officers_on_light_duty = models.IntegerField(blank=True, default=0)
    officers_out_sick = models.IntegerField(blank=True, default=0)
    officers_in_training = models.IntegerField(blank=True, default=0)
    officers_on_vacation = models.IntegerField(blank=True, default=0)
    officers_assigned_elswhere = models.IntegerField(blank=True, default=0)
    total_citations_issued = models.IntegerField(blank=True, default=0)
    total_warnings_issued = models.IntegerField(blank=True, default=0)
    total_citizen_contacts = models.IntegerField(blank=True, default=0)
    total_traffic_stops = models.IntegerField(blank=True, default=0)
    total_arrest_made = models.IntegerField(blank=True, default=0)
    total_juvenile_contacts = models.IntegerField(blank=True, default=0)
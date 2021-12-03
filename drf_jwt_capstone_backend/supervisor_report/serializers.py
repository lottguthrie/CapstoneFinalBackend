from rest_framework import serializers 
from .models import SupervisorReport  
    

class SupervisorReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupervisorReport
        fields = ( 'supervisor_report_id', 'supervisor_id',
        'date', 'total_calls_for_service', 'total_case_numbers_pulled',
        'total_case_numbers_completed', 'total_reports','total_supplements',
        'total_vehicles_assigned', 'total_miles_driven', 'officers_on_road', 
        'officers_on_desk', 'officers_on_jail_duty', 'officers_on_light_duty',
        'officers_out_sick', 'officers_in_training', 'officers_on_vacation',
        'officers_assigned_elswhere', 'total_citations_issued', 'total_warnings_issued',
        'total_citizen_contacts', 'total_traffic_stops','total_arrest_made'
        'total_juvenile_contacts' )
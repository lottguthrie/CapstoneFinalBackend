from rest_framework import serializers
from .models import DailyReport


class DailyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyReport
        fields = ( 'report_id', 'officer_id', 'date', 
        'calls_for_service','reports', 'supplements', 'citations_issued',
        'warnings_issued', 'traffic_stops', 'citizen_contacts', 'juvenile_contacts',
        'assigned_area', 'assigned_vehicle', 'miles_driven', 'hours_worked', 'case_numbers' )
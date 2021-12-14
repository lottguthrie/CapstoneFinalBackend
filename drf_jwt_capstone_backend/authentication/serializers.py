from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from .models import DailyReport
from .models import SupervisorReport 
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken

Registration = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[
                                   UniqueValidator(queryset=Registration.objects.all())])

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = Registration

        fields = ( 'password',   'last_login', 'is_superuser','username', 'first_name', 'last_name', 'email',
                'is_staff', 'is_active', 'date_joined', 'middle_name', 'phone_number', 'badge_number', 'officer_id',
                'supervisor_id'
                 )

    def create(self, validated_data):

        registration = Registration.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            middle_name=validated_data['middle_name'],

        )
        registration.set_password(validated_data['password'])
        registration.save()

        return registration

class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    officer_id = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = User
        fields = ( 'password', 'last_login', 'is_superuser','username', 'first_name', 'last_name', 'email',
                'is_staff', 'is_active', 'date_joined', 'middle_name', 'phone_number', 'badge_number', 'officer_id',
                'supervisor_id'
                 )
        
    def get__officerid(self, obj):
        return obj.officer_id
        
    def get_isAdmin(self, obj):
        return obj.is_staff
        
    def get_name(self, obj):
        name = obj.first_name
        if name == '':
            name = obj.email
            return name

    


class UserSerailizerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'officer_id', 'password', 'last_login', 'is_superuser','username', 'first_name', 'last_name', 'email',
                'is_staff', 'is_active', 'date_joined', 'middle_name', 'phone_number', 'badge_number', 'officer_id',
                'supervisor_id', 'token']
                 

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)
    
class DailyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyReport
        fields = ['report_id', 'officer_id', 'date', 'calls_for_service', 'reports', 'supplements',
        'citations_issued', 'warnings_issued', 'traffic_stops', 'citizen_contacts', 'juvenile_contacts',
        'assigned_area', 'assigned_vehicle', 'miles_driven', 'hours_worked', 'case_numbers']

        def get_DailyReport(self, obj):
            DailyReports = obj.DailyReport_set.all()
            serializer = DailyReport(DailyReports, many=True)
            return serializer.data


Supervisor = get_user_model()


class SupervisorSerializer(serializers.ModelSerializer):
    supervisor_Id = serializers.IntegerField(required=True, validators=[
                                   UniqueValidator(queryset=Supervisor.objects.all())])

    supervisor_password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = Supervisor
        fields = ('supervisor_id', 'officer_id', 'supervisor_reportid', 'last_name', 'first_name'
        'middle_name', 'badge_number')

    def create(self, validated_data):

        supervisors = Supervisor.objects.create(
            supervisor_id=validated_data['supervisor_id'],
            officer_id=validated_data['officer_id'],
            supervisor_reportid=validated_data['supervisor_reportid'],
            last_name=validated_data['last_name'],
            first_name=validated_data['first_name'],
            middle_name=validated_data['middle_name'],
            badge_number=validated_data['badge_number']


        )
        supervisors.set_password(validated_data['supervisor_password'])
        Supervisor.save()

        return Supervisor     


from .models import SupervisorReport  
    

class SupervisorReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupervisorReport
        fields = ['supervisor_report_id', 'supervisor_id', 'date', 'total_calls_for_service',
    'total_case_numbers_pulled', 'total_case_numbers_completed', 'total_reports', 'total_supplements', 
    'total_vehicles_assigned', 'total_miles_driven', 'officers_on_road', 'officers_on_desk',
    'officers_on_jail_duty', 'officers_on_light_duty', 'officers_out_sick', 'officers_in_training',
    'officers_on_vacation', 'officers_assigned_elswhere', 'total_citations_issued', 'total_warnings_issued',
    'total_citizen_contacts', 'total_traffic_stops', 'total_arrest_made', 'total_juvenile_contacts']

        def get_SupervisorReport(self, obj):
            SupervisorReports = obj.SupervisorReport_set.all()
            serializer = SupervisorReport(SupervisorReports, many=True)
            return serializer.data
       
        
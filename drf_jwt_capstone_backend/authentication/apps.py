from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentication'

class DailyReportConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'DailyReport'

class SupervisorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Supervisor'

    
class SupervisorReportConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'SupervisorReport'
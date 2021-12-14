from django.contrib import admin
from .models import *
# from drf_jwt_capstone_backend.authentication.serializers import User

# Register your models here.
admin.site.register(User)
admin.site.register(DailyReport)
admin.site.register(Supervisor)
admin.site.register(SupervisorReport)

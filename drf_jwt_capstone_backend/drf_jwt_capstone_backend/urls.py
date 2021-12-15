
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('api/authentication/', include('authentication.urls.officer_views_urls')),    
    path('api/daily_report/', include('authentication.urls.daily_report_urls')),
    path('api/supervisor/', include('authentication.urls.supervisor_views_urls')),
    path('api/supervisor_report/', include('authentication.urls.supervisor_report_urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



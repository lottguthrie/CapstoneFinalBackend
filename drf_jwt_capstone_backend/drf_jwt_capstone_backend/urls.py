from django.contrib import admin
from django.urls import path, include
from authentication import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('api/officer_views/', TemplateView.as_view(template_name='index.html')),
    path('api/daily_report_views/',TemplateView.as_view(template_name='index.html')),
    path('api/supervisor_views/', TemplateView.as_view(template_name='index.html')),
    path('api/supervisor_report_view/',TemplateView.as_view(template_name='index.html')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
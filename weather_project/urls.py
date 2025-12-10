from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='demo.html')),  # ✅ ONE SINGLE DEMO PAGE
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
]

from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('school/', include('school.urls')),
    path('', RedirectView.as_view(url='/school/students/', permanent=False)),
]

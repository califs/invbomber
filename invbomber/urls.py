from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # Agrega esta línea
from django.conf.urls.static import static  # Agrega esta línea

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bomberos.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
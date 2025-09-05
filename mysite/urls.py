from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_home.urls')),
    path('webdocs/', include('app_webdoc.urls')),
]

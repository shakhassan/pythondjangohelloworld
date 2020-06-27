from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('boards/', include('boards.urls')),
    path('admin/', admin.site.urls),
]

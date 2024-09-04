from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from crm import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crm.urls'))
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

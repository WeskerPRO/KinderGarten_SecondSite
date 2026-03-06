from django.contrib import admin
from django.urls import path
from main import views
from django.conf.urls.static import static
from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),  # READY AUTH DONE!
    path('', views.about, name="about"),  # DONE!
    path('staff/', views.staff, name="staff"),  # DONE!
    path('news/', views.news, name="news"),  # DONE!
    path('galary/', views.galary, name="galary"),  # DONE!
    path('contact/', views.contact, name="contact")  # DONE!
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

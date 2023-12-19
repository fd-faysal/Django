
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', views.contact),
    path('newapp/', include("newapp.urls")),
    path('',views.Home),
]

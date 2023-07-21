from django.urls import path,include
from . import views
urlpatterns = [
    path('index', views.index,name='home'),
    path('about', views.about,name='about'),
    path('booking', views.booking,name='booking'),
    path('doctors', views.doctors,name='doctors'),
    path('contacts', views.contacts,name='contacts'),
    path('departments',views.departments,name='departments'),

]
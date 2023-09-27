from django.urls import path

from . import views


app_name = 'account'
urlpatterns = [
    path('doctor/', views.doctor_list, name='doctor_list')
]

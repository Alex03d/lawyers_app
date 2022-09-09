from django.urls import path

from . import views


app_name = 'contracts'


urlpatterns = [
    path('', views.index, name='index'),
    path('contracts_list/', views.contracts_list, name='contracts_list')
]
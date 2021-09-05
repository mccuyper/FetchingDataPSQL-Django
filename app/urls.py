from django.urls import path, include
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.showdata), 
    path('download-csv', views.generate_csv, name='generate-csv'), 
    # path('', DBView.as_view(), name='db_fetch'),
]

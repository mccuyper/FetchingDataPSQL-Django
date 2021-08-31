from django.urls import path, include
from django.conf.urls import url
from . import views
from app import save2csv

urlpatterns = [
    path('', views.showdata),  

    # path('', DBView.as_view(), name='db_fetch'),
]

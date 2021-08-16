from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.showdata),  
    # path('', DBView.as_view(), name='db_fetch'),
]

from django.shortcuts import render
from app.models import FetchIt

def showdata(request):
    results = FetchIt.objects.all()
    return render(request, 'index.html',{"data":results})
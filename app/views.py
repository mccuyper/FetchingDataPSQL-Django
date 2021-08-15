from django.shortcuts import render
from app.models import FetchIt

def showdata(request):
    results = FetchIt.objects.all()
    item_name = request.GET.get('item_name')

    if item_name != '' and item_name is not None:
        results = results.filter(d_name__icontains=item_name, direction__icontains='out') # shows up all outgoing direction
   
    return render(request, 'index.html',{"data":results})

from django.shortcuts import render
from django.http import HttpResponse
from app.models import FetchIt
from django.db.models import Sum
from bs4 import BeautifulSoup
import urllib.request
import csv
import requests


def showdata(request):
    results = FetchIt.objects.all()
    domains = results.distinct('d_name')
    item_name = request.GET.get('item_name')
    month = request.GET.get('month')
    total = FetchIt.objects.aggregate(Sum('duration'))['duration__sum']
    total = total/60
    if item_name != '' and item_name is not None and month != '' and month is not None:
        results = results.filter(d_name__icontains=item_name, direction__icontains='out', created_on__icontains='2021-'+month)
        total = results.aggregate(Sum('duration'))['duration__sum']
        total = total/60
   
    context = {
        "data":results,
        "dom_names":domains,
        'total': total,
    }

    return render(request, 'index.html',context )

def generate_csv(request):
    url = request.META.get('HTTP_REFERER')
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.select_one("table")
    headers = [th.text for th in table.select("tr th")]
    
    with open("result.csv", "w", newline="") as f:
        wr = csv.writer(f, quoting=csv.QUOTE_ALL)
        wr.writerow(headers)
        wr.writerows([[td.text for td in row.find_all("td")] for row in table.select("tr + tr")])

    with open("result.csv") as f:
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=result.csv'    
        writer = csv.writer(response)
        
        return response



def showByDomains(request):
    return HttpResponse("<h1>REDIRECTED</h1>")
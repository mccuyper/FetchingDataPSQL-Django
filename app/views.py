from django.shortcuts import render
from app.models import FetchIt



def showdata(request):
    results = FetchIt.objects.all()
    domains = results.distinct('d_name')
    item_name = request.GET.get('item_name')
    month = request.GET.get('month')

    if item_name != '' and item_name is not None:
        results = results.filter(d_name__icontains=item_name, direction__icontains='out')

    if month != '' and month is not None:
        results = results.filter(created_on__icontains='2021-'+month, direction__icontains='out')

    return render(request, 'index.html',{"data":results, "dom_names":domains})


# # -----class based view------
# from django.db.models import Q
# from django.views.generic import ListView

# class DBView(ListView):
#     model = FetchIt
#     template_name = 'index.html'
#     context_objects_name = 'data'
#     paginate_by = 100

#     def get_queryset(self):
#         item_name = self.request.GET.get('item_name', '')
#         month = self.request.GET.get('month', '')
#         object_list = FetchIt.objects.filter(
#             Q(d_name__icontains=item_name) 
#              | Q(created_on__icontains=month)
#         )
#         return object_list

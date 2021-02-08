from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    my_dict = {'weekNumber': 2}
    return render(request, 'simple_app/static.html', context = my_dict)
    #return HttpResponse("Hello World!!")
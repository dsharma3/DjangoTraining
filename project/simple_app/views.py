from django.shortcuts import render
from django.http import HttpResponse
from simple_app.models import Website
# Create your views here.
def index(request):
    my_dict = {'weekNumber': 2}
    return render(request, 'simple_app/static.html', context = my_dict)
    #return HttpResponse("Hello World!!")

def display_websites(request):
    website_list = Website.objects.all()
    my_dict = {'websites':website_list}
    return render(request, 'simple_app/modelBinding.html', context = my_dict)
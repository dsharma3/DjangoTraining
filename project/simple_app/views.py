from django.shortcuts import render
from django.http import HttpResponse
from simple_app.models import Website
from simple_app.form import ContactForm
# Create your views here.
def index(request):
    my_dict = {'weekNumber': 2}
    return render(request, 'simple_app/static.html', context = my_dict)
    #return HttpResponse("Hello World!!")

def display_websites(request):
    website_list = Website.objects.all()
    my_dict = {'websites':website_list}
    return render(request, 'simple_app/modelBinding.html', context = my_dict)

def contact_us(request):
    return render(request, 'simple_app/contactus.html')


def contact_us_django(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data['contactname']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
                
            print("Name-",name)
            print("Email-",email)
            print("Message-",message)           
    
    return render(request, 'simple_app/contactus-django.html', {'form':form})
    

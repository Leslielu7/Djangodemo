from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home/welcome.html',{'today':datetime.today()})

#display the authorized.html template
@login_required(login_url='admin/')#add this function as a decorator of the function authorized
def authorized(request):
    return render(request, 'home/authorized.html', {})
import re
from django.utils.timezone import datetime
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(
        request,
        'login/home.html',
    )

def login_data(request, name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d, %B, %Y at %X")
    match_object = re.match("[a-zA-Z]+",name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "\n It's " + formatted_now
    return HttpResponse(content)

def login_user(request):
    return render(
        request,
        'login/login_user.html',
        {
            #'name':name,
            'date':datetime.now()
        }
    )
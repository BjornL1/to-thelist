from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def test_authentication(request):
    return HttpResponse("Test user authentication")


def home(request):
    return render(request, 'index.html')


def about(request):
    return HttpResponse("About")

def input_form_view(request):
    return render(request, 'input_form.html')

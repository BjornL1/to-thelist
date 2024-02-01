from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def test_authentication(request):
    return HttpResponse("Test user authentication")

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def index(request):
    template = loader.get_template('restaurants/index.html')
    return HttpResponse(template.render({}, request))

def detail(request, restaurant_id):
    return HttpResponse("You're looking at restaurant %s." % restaurant_id)

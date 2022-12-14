from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, Http404

from .models import Restaurant, Dish, Review

# Create your views here.
def index(request):
    # template = loader.get_template('restaurants/index.html')
    all_restaurants = Restaurant.objects.all()
    context = {
        'all_restaurants': all_restaurants,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'restaurants/index.html', context)

def detail(request, restaurant_id):
    # try:
    #     restaurant = Restaurant.objects.get(pk=restaurant_id)
    # except Restaurant.DoesNotExist:
    #     raise Http404("Restaurant does not exist sorry buddy")
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    return render(request, 'restaurants/detail.html', {'restaurant': restaurant})

def comment(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    try:
        rating = int(request.POST['rating'])
        comment = request.POST['comment']
    except (KeyError, ValueError):
        return render(request, 'restaurants/detail.html', {
            'restaurant': restaurant,
            'error_message': "You didn't provide a rating or a comment",
        })
    else:
        Review.objects.create(restaurant=restaurant, rating=rating, comment=comment)
        return render(request, 'restaurants/detail.html', {'restaurant': restaurant})

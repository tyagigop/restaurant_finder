from django.shortcuts import render, get_object_or_404
import csv
import json
from .models import *


def home(request):
    query = request.GET.get('query')

    if query:
        x1 = Restaurant.objects.filter(items__icontains=query)
    else:
        x1 = Restaurant.objects.all()

    context = {
        'x1': x1,
    }

    return render(request, 'index.html', context)


def details(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    context = {'restaurant': restaurant}
    return render(request, 'details.html', context)


def menu_details(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)

    test_dict = restaurant.items
    

    res1 = dict(list(test_dict.items())[len(test_dict)//2:])
    res2 = dict(list(test_dict.items())[:len(test_dict)//2])

    context = {
        'restaurant': restaurant,
        'res1' : res1,
        'res2' : res2,
        
    }

    return render(request, 'menu_details.html', context)

def createdata():
    with open('home/restaurants_small.csv') as file_data:
        file_d = csv.DictReader(file_data)
        x = list(file_d)

    for i in x:
        id = i['id']
        name = i['name']
        location = i['location']

        lat_long = i['lat_long']

        if i['items'] != '':
            items = json.loads(i['items'])

        if i['full_details'] != '':
            full_details = json.loads(i['full_details'])

        Restaurant.objects.create(
            id=id,
            name=name,
            location=location,
            lat_long=lat_long,
            items=items,
            full_details=full_details,
        )

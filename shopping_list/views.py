from django.shortcuts import render
from .models import ShoppingList

# Create your views here.


def shopping_list_view(request):
    # Retrieve all shopping list items from the database
    shopping_list = ShoppingList.objects.all()

    # Render the template with the shopping list data
    return render(request, 'shopping_list.html', {'shopping_list': shopping_list})


def input_form_view(request):
    # Simply render the input_form.html template
    return render(request, 'input_form.html')

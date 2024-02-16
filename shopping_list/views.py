from django.shortcuts import render
from .forms import ItemForm  # Import your ItemForm
from .models import ShoppingList

def input_form_view(request):
    if request.method == 'POST':  # Check if the request method is POST
        form = ItemForm(request.POST)  # Create a form instance with POST data
        if form.is_valid():  # Check if the form data is valid
            form.save()  # Save the form data to the database
    else:  # If the request method is not POST
        form = ItemForm()  # Create a blank form instance

    shopping_list = ShoppingList.objects.all()  # Retrieve all shopping list items
    return render(request, 'input_form.html', {'form': form, 'shopping_list': shopping_list})
'''
from django.shortcuts import render, redirect
return redirect('success_url')  # Redirect to a success page after saving

---------
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
'''



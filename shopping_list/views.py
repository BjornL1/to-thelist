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



# from django.shortcuts import render, redirect
# from .forms import ItemForm  # Import your ItemForm

# def input_form_view(request):
#    if request.method == 'POST':
#        form = ItemForm(request.POST)
#        if form.is_valid():
#            form.save()  # Save the form data to the database
#            return redirect('success_url')  # Redirect to a success page after saving
#    else:
#        form = ItemForm()
#    return render(request, 'input_form.html', {'form': form})
# from django.shortcuts import render, redirect
# from .forms import ItemForm  # Import your ItemForm
# from .models import ShoppingList

# def input_form_view(request):
#    if request.method == 'POST':
#        form = ItemForm(request.POST)
#        if form.is_valid():
#           form.save()  # Save the form data to the database
#           return redirect('success_url')  # Redirect to a success page after saving
#   else:
#       form = ItemForm()
#   shopping_list = ShoppingList.objects.all()  # Retrieve all shopping list items
#   return render(request, 'input_form.html', {'form': form, 'shopping_list': shopping_list})
from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['list_name', 'item_name']  # Assuming 'list_name' and 'item_name' are the fields for the list name and item name
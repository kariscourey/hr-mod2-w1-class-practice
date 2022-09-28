from django.db import render
from .models import Cart

def add_item_in_cart(cart_id, sku):
    cart = Cart.objects.get(id=cart_id)
    # isolating functions within our model
    # otherwise, would have to put all add_item functionality here
    # would be messy and hard to maintain
    cart.add_item(sku)

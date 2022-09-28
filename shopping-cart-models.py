from django.db import models

class ProductVO(models.Model):
    sku = models.CharFied(max_length=255, unique=True)

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    cart_items = models.ManytoManyRel(CartItem)

    def get_cartItems(self):
        return cart_items

    def add_item(self, sku):
        product = ProductVO.objects.get(sku=sku)
        cart_items = self.cart_item.objects.filter(product=product)  # get cart items related to product
        if len(cart_items) == 1:
            cart_item = cart_item[0]
            cart_item[0].quantity += 1
            cart_item.save()
        else:
            CartItem.objects.create(product=product,sku=sku,cart=self,quantity=1)

    def delete_item(self, sku):
        product = ProductVO.objects.get(sku=sku)
        self.cart_items.filter(product=product).delete()
        # working through products, controlled as part of products

    def increment_item(self, sku):
        product = ProductVO.objects.get(sku=sku)
        cart_item = self.cart_items.objects.get(product=product)
        cart_item.quantity += 1
        cart_item.save()
        # working through products, controlled as part of products


    def decrement_item(self, sku):
        product = ProductVO.objects.get(sku=sku)
        cart_item = self.cart_items.objects.get(product=product)
        cart_item.quantity -= 1
        if cart_item.quantity == 0:
            cart_item.delete()
        else:
            cart_item.save()
        # working through products, controlled as part of products


    # buy now = cartless, bypasses cart


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductVO, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()

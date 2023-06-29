from product.models import Basket

basket = Basket.objects.create(user=bot_user_instance, product=product_instance, count=5, price=10)


basket = Basket.objects.get(user=bot_user_instance)
basket.delete()

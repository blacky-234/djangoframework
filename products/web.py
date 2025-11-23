from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Category
from django.core.cache import cache


# These views only render templates. JS handles API calls.
class ProductManaging:

    def select_inventory(request):
        return render(request, "home/select_inventory.html")
    
    def list_category(request):
        category = cache.get("category")

        if not category:
            category = Category.objects.all().order_by('-id')
            cache.set("category", category, 60)
        return render(request, "category/list.html",{"categories":category})
   
    @ensure_csrf_cookie
    def products_page(request):
        context = {}
        context["categories"] = Category.objects.all()
        return render(request, "product.html",context)

    @ensure_csrf_cookie
    def product_form_page(request):
        # used for create & update; update will pass ?id=...
        return render(request, "myapp/product_form.html")

    @ensure_csrf_cookie
    def orders_page(request):
        return render(request, "myapp/orders.html")

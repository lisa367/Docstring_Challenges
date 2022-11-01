from django.shortcuts import render
from store.models import Product

# Create your views here.


def index(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "store/index.html", context=context)


def detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, "store/detail.html", context={"product": product})

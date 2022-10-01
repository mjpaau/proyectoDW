from django.shortcuts import render

from core.erp.models import Category, Product


# Create your views here.
def myfirstview(request):
    data = {
        'name': 'Moises',
        'categories': Category.objects.all()
    }
    return render(request, 'index.html', data)


def mysecondview(request):
    data = {
        'name': 'Moises',
        'products': Product.objects.all()
    }
    return render(request, 'second.html', data)
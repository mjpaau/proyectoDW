from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from core.erp.models import Category, Product


def category_list(request):

    data = {
        'title': 'Listado de Categorías',
        'categories': Category.objects.all()
    }
    return render(request,'category/list.html', data)

class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'

    # def get_queryset(self):
    #     return Category.objects.filter(name__startswith='L')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {'name': 'William'}
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorias'
        return context
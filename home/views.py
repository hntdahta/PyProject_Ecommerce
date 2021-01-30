from django.http import HttpResponse
from django.shortcuts import render
from home.models import Clothes
from home.models import Category
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    clothes = Clothes.objects.all()
    clothes_paginator = Paginator(clothes, 6)
    page_num = request.GET.get('page')
    page = clothes_paginator.get_page(page_num)
    Data = {
        'Clothes': Clothes.objects.all(),
        'count' : clothes_paginator.count,
        'page' : page
    }
    return render(request, 'home/index.html', Data)

def detail(request, id):
    clothes = Clothes.objects.get(id=id)
    return render(request, 'home/shop-single.html', {'Clothes':clothes})

def category(request, id):
    category = Category.objects.filter(id=id)
    return render(request, 'home/portfolio-category.html', {'Category':category})

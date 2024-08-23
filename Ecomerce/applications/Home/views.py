from django.shortcuts import render
from django.views.generic import TemplateView
from applications.Products.models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.




class IndexTemplateView(TemplateView):
    template_name = "Home/index.html"


def indexProductsView(request):
    products = Product.objects.getProducts()

    paginator = Paginator(products, 10)

    page = request.GET.get('page')

    try:
        products_paginated = paginator.page(page)
    except PageNotAnInteger:
        products_paginated = paginator.page(1)
    except EmptyPage:
        products_paginated = paginator.page(paginator.num_pages)
    

    context = {
        'products':products_paginated
    }

    return render(
        request,
        "Home/index.html",
        context
    )
    

from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import Category, Product, Contact
from cart.forms import CartAddProductForm
from .forms import ContactForm
from django.views.generic import View
from django.http.response import HttpResponse, HttpResponseRedirect


def index(request):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    trending_products = Product.objects.filter(trending=1)
    return render(request, 'shop/index.html', context={
        'category': category,
        'categories': categories,
        'products': products,
        'trending_products': trending_products})

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render (request, 'shop/product/list.html', context={
        'category': category,
        'categories': categories,
        'products': products,
    })

def product_detail(request, id, slug):
    trending_products = Product.objects.filter(trending=1)
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()

    context = {'product':product,
               'cart_product_form':cart_product_form,
               'trending_products':trending_products}

    return render(request, 'shop/product/detail.html', context)



def questions_answer(request):
    return render(request, "shop/information/questions_answer.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST or None)
        errors = None
        if form.is_valid():
            Contact.objects.create(
                first_name = form.cleaned_data.get('first_name'),
                last_name = form.cleaned_data.get('last_name'),
                email = form.cleaned_data.get('email'),
                message = form.cleaned_data.get('message')
                )
            messages.warning(request,"Запит на зворотний зв'язок надіслано. Очікуйте...")
            return render(request,"shop/information/contacts.html")
        if form.errors:
            errors = form.errors

        context = {'form':form, 'errors':errors}
        return render(request,"shop/information/contacts.html", context )
    else:
        form = ContactForm()

    return render(request, "shop/information/contacts.html", {'form':form})


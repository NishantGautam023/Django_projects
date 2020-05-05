from django.shortcuts import render

# Create your views here.

# creating a function based view


def store(request):
    context = {}  # creating a context dictionary where we will pass some data, making empty for now
    return render([request], ['store/store.html'], [context])


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)


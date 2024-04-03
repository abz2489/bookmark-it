from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from . import views
from books.models import Book


def view_basket(request):
    """A view that renders basket items page"""

    return render(request, "basket/basket.html")


def add_to_basket(request, book_id):
    """Add book quantity to basket"""

    book = get_object_or_404(Book, id=book_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if book_id in list(basket.keys()):
        basket[book_id] += quantity
        messages.success(request, f'Updated {book.title} quantity to {basket[book_id]}')
    else:
        basket[book_id] = quantity
        messages.success(request, f'Added {book.title} by {book.author} to your basket')

    request.session['basket'] = basket
    print(request.session['basket'])
    return redirect(redirect_url)
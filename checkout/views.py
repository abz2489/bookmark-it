from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404,
    HttpResponse
)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from books.models import Book
from basket.contexts import basket_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'basket': json.dumps(request.session.get('basket', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, "Sorry, we're having trouble processing \
            your payment right now. Please try again later.")
        return HttpResponse(content=e, status=400)


def checkout(request):

    """A view to display checkout page, load basket and order form"""

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        basket = request.session.get('basket', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        # If the form is valid, save data
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_basket = json.dumps(basket)
            order.save()

            # Create new order line item for each book in basket
            for book_id, book_data in basket.items():
                try:
                    book = Book.objects.get(id=book_id)
                    if isinstance(book_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            book=book,
                            quantity=book_data,
                        )
                        order_line_item.save()

                # If a book isn't found
                # Delete empty order and return to basket
                except Book.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your basket \
                         wasn't found in our database."
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_basket'))

            # If order is successful, show checkout success page
            # If form is invalid, display error message to user
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse(
                'checkout_success', args=[order.order_number]))
        else:
            messages.error(request, "There was an error with your form. \
                Please double check your information.")

    else:
        basket = request.session.get('basket', {})
        if not basket:
            messages.error(request, 'Your basket is empty!')
            return redirect(reverse('books'))

        current_basket = basket_contents(request)
        total = current_basket['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY
        )

        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, "The Stripe public key is missing. \
            Make sure the public key is set in your environement.")

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order processed successfully! \
        Your order number is {order_number}. A confirmation \
            email will be sent to {order.email}.')

    if "basket" in request.session:
        del request.session["basket"]

    template = "checkout/checkout_success.html"
    context = {
        "order": order,
    }
    return render(request, template, context)
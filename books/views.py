from unicodedata import category
from django.shortcuts import render,get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Category, Book


def all_books(request):
    """A view to return the books, sorting & search queries"""

    books = Book.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    """Search queries, sorting by title, author, price and category"""
    if request.GET:
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "title":
                print(f"Sort Key: {sortkey}")
                sortkey = "lower_title"
                books = books.annotate(lower_title=Lower("title"))

            if sortkey == "author":
                sortkey = "lower_author"
                books = books.annotate(lower_author=Lower("author"))

            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            books = books.order_by(sortkey)

        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            books = books.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if "q" in request.GET:
            query = request.GET["q"]
            print(f"Query: {query}")
            if not query:
                messages.error(request, "No search criteria entered!")
                return redirect(reverse("books"))
            
            queries = Q(title__icontains=query) | Q(author__icontains=query) | Q(summary__icontains=query) | Q(category__name__icontains=query)
            books = books.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        "books": books,
        "search_term": query,
        "current_categories": categories,
        "current_sorting": current_sorting
    }
    return render(request, "books/books.html", context)


def book_summary(request, book_id):
    """This view displays an individual summary of a selected book"""

    book = get_object_or_404(Book, id=book_id)

    context = {
        "book": book,
    }
    return render(request, "books/book_summary.html", context)
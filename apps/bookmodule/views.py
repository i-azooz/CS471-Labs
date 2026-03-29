from django.shortcuts import render
from django.http import HttpResponse

# --- دوال اللاب الرابع (الجديد) ---
def index(request):
    return render(request, "bookmodule/index.html")

def list_books(request):
    return render(request, 'bookmodule/list_books.html')

def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

# --- دالة اللاب القديم (عشان يختفي الخطأ) ---
def add(request, n1, n2):
    return HttpResponse(str(n1 + n2))
    def links_view(request):
    return render(request, 'bookmodule/links.html')

def formatting_view(request):
    return render(request, 'bookmodule/formatting.html')

def listing_view(request):
    return render(request, 'bookmodule/listing.html')

def tables_view(request):
    return render(request, 'bookmodule/tables.html')

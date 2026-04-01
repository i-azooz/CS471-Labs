from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("Hello, world!")
def links_view(request):
    return render(request, 'bookmodule/links.html')

def tables_view(request):
    return render(request, 'bookmodule/tables.html')

def listing_view(request):
    return render(request, 'bookmodule/listing.html')
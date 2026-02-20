from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("Hello, world!")
def viewbook(request, bookId):
    return HttpResponse(f"The book id is: {bookId}")
def add(request, n1, n2):
    res = n1 + n2
    return HttpResponse(f"The sum is: {res}")

from django.shortcuts import render, HttpResponse
from .models import Book  


def index(request):
    return HttpResponse("Hello, world!")
def links_view(request):
    return render(request, 'bookmodule/links.html')

def tables_view(request):
    return render(request, 'bookmodule/tables.html')

def listing_view(request):
    return render(request, 'bookmodule/listing.html')

def search(request):
    if request.method == "POST":
        keyword = request.POST.get('keyword').lower() # جلب الكلمة
        isTitle = request.POST.get('option1')        # اختيار العنوان
        isAuthor = request.POST.get('option2')       # اختيار المؤلف
        
        books = getBooksList() # جلب قائمة الكتب اللي تحت
        newBooks = []
        
        for item in books:
            contained = False
            if isTitle and keyword in item['title'].lower(): contained = True
            if not contained and isAuthor and keyword in item['author'].lower(): contained = True
            
            if contained:
                newBooks.append(item)
        
        return render(request, 'bookmodule/bookList.html', {'books': newBooks})
        
    return render(request, 'bookmodule/search.html')

def getBooksList():
    book1 = {'id': 12344321, 'title': 'Continuous Delivery', 'author': 'J.Humble and D. Farley'}
    book2 = {'id': 56788765, 'title': 'Reversing: Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    book3 = {'id': 43211234, 'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov'}
    return [book1, book2, book3]

def bookList(request):
    render_context = {'books': getBooksList()}
    return render(request, 'bookmodule/bookList.html', render_context)



def lab7_insert_data(request):
    Book.objects.create(title='Continuous Delivery', author='J.Humble and D. Farley', price=120.0, edition=3)

    Book.objects.create(title='Reversing: Secrets of Reverse Engineer', author='E. Eilam', price=97.0, edition=2)


    Book.objects.create(title='The Hundred-Page Machine Learning Book', author='Andriy Burkov', price=100.0, edition=4)
    
    Book.objects.create(title='Django and Python Web Development', author='Abdulaziz', price=150.0, edition=2)

    return HttpResponse("Data Inserted Successfully!")

def simple_query(request):
    
   mybooks = Book.objects.filter(title__icontains='and') 
   return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def complex_query(request):
    mybooks = Book.objects.filter(author__isnull=False).filter(title__icontains='and').filter(edition__gte=2)
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})


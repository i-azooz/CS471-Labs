from django.shortcuts import render, HttpResponse
from django.db.models import Q, Avg, Sum, Max, Min
from .models import Book, Student  


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

def lab8_task1(request):
    books = Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/lab8_task1.html', {'books': books})

def lab8_task2(request):
    books = Book.objects.filter(Q(edition__gt=3) & (Q(title__icontains='qu') | Q(author__icontains='qu')))
    return render(request, 'bookmodule/lab8_task2.html', {'books': books})

def lab8_task3(request):
    books = Book.objects.filter(~(Q(edition__gt=3) & (Q(title__icontains='qu') | Q(author__icontains='qu'))))
    return render(request, 'bookmodule/lab8_task3.html', {'books': books})

def lab8_task4(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/lab8_task4.html', {'books': books})

def lab8_task5(request):
    books = Book.objects.all()
    total_price = books.aggregate(Sum('price'))['price__sum']
    avg_price = books.aggregate(Avg('price'))['price__avg']
    max_price = books.aggregate(Max('price'))['price__max']
    min_price = books.aggregate(Min('price'))['price__min']
    return render(request, 'bookmodule/lab8_task5.html', {'total_price': total_price, 'avg_price': avg_price, 'max_price': max_price, 'min_price': min_price})

def lab8_task7(request):
    students = Student.objects.filter(address__city__istartswith='R')
    return render(request, 'bookmodule/lab8_task7.html', {'students': students})






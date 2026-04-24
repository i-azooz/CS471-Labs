from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"), # الصفحة الرئيسية (Hello World)
    path('html5/links/', views.links_view, name="books.links"),
    path('html5/tables/', views.tables_view, name="books.tables"),
    path('html5/listing/', views.listing_view, name="books.listing"),
    path('search/', views.search, name="bookmodule-search"),
    path('bookList/', views.bookList, name="bookList"),
    path('lab7/insert/', views.lab7_insert_data),
    path('lab7/query/', views.simple_query),
    path('lab7/complexquery/', views.complex_query),
   path('books/lab8/task1', views.lab8_task1, name='lab8_task1'),
path('books/lab8/task2', views.lab8_task2, name='lab8_task2'),
path('books/lab8/task3', views.lab8_task3, name='lab8_task3'),
path('books/lab8/task4', views.lab8_task4, name='lab8_task4'),
path('books/lab8/task5', views.lab8_task5, name='lab8_task5'),
path('books/lab8/task7', views.lab8_task7, name='lab8_task7'),
    



]

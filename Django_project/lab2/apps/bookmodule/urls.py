from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"), # الصفحة الرئيسية (Hello World)
    path('html5/links/', views.links_view, name="books.links"),
    path('html5/tables/', views.tables_view, name="books.tables"),
    path('html5/listing/', views.listing_view, name="books.listing"),
]
from django.contrib import admin
from .models import Publisher, Author, Book # تأكد من استيرادهم كلهم

admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)
# Register your models here.

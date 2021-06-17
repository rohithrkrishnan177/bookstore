from django.contrib import admin
from .models import Book,Cart,Customer

# Register your models here.
admin.site.register(Book)
admin.site.register(Cart)
admin.site.register(Customer)
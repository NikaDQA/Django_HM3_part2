from django.contrib import admin
from .models import Book, LibraryUser, BorrowedBook


admin.site.register(Book)
admin.site.register(LibraryUser)
admin.site.register(BorrowedBook)

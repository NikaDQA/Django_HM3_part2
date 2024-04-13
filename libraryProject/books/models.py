from django.db import models




class Book(models.Model):
    name = models.CharField(max_length=256)
    is_available = models.BooleanField(default=True)


class LibraryUser(models.Model):
    name = models.CharField(max_length=256)
    book = models.ForeignKey(Book, on_delete=models.CASCADE,null=True, blank=True)
    is_author = models.BooleanField(default=False)


class BorrowedBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey(LibraryUser, on_delete=models.CASCADE)
    borrowed_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
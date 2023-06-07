from django.db import models

# Create your models here.
class Books(models.Model):
    id                  = models.TextField(primary_key=True)
    title               = models.TextField()
    author              = models.TextField()
    publication_date    = models.DateField(blank=True, null=True)
    insert_date         = models.TextField(blank=True, null=True)  # This field type is a guess.
    updated_at          = models.TextField(blank=True, null=True)  # This field type is a guess.

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'books'

class CategoryBooks(models.Model):
    nama_kategori = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'category_books'

class StatusBooks(models.Model):
    name_status = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'status_books'

class BorrowBook(models.Model):
    id = models.TextField(primary_key=True)  # This field type is a guess.
    id_category = models.ForeignKey(CategoryBooks, on_delete=models.CASCADE)
    id_status_books = models.ForeignKey(StatusBooks, on_delete=models.CASCADE)
    id_books = models.TextField(blank=True, null=True)  # This field type is a guess.
    username = models.TextField(blank=True, null=True)
    title = models.TextField()
    author = models.TextField()
    publication_date = models.DateField(blank=True, null=True)
    borrow_date = models.DateField(blank=True, null=True)
    status_borrow = models.TextField(blank=True, null=True)  # This field type is a guess.
    status_return = models.TextField(blank=True, null=True)  # This field type is a guess.c

    def __str__(self):
        return self.name
    

    class Meta:
        managed = False
        db_table = 'borrow_book'
    
class ConfirmBorrowBook(models.Model):
    id = models.TextField(primary_key=True)  # This field type is a guess.
    id_category = models.ForeignKey(CategoryBooks, on_delete=models.CASCADE)
    id_status_books = models.ForeignKey(StatusBooks, on_delete=models.CASCADE)
    id_books = models.TextField(blank=True, null=True)  # This field type is a guess.
    username = models.TextField(blank=True, null=True)
    title = models.TextField()
    author = models.TextField()
    publication_date = models.DateField(blank=True, null=True)
    borrow_date = models.DateField(blank=True, null=True)
    status_borrow = models.TextField(blank=True, null=True)  # This field type is a guess.
    status_return = models.TextField(blank=True, null=True)  # This field type is a guess.c

    def __str__(self):
        return self.name
    

    class Meta:
        managed = False
        db_table = 'borrow_book'

class AuthUser(models.Model):
    password        = models.CharField(max_length=128)
    last_login      = models.DateTimeField(blank=True, null=True)
    is_superuser    = models.BooleanField()
    username        = models.CharField(unique=True, max_length=150)
    last_name       = models.CharField(max_length=150)
    email           = models.CharField(max_length=254)
    is_staff        = models.BooleanField()
    is_active       = models.BooleanField()
    date_joined     = models.DateTimeField()
    first_name      = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'

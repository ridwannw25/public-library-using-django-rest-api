from django.urls import path
from . import views



urlpatterns = [
    path('FindBook', views.FindBook.as_view(), name="FindBook"),
    path('BorrowBook', views.BorrowBook.as_view(), name="BorrowBookLibrary"),
    path('ConfirmBookBorrow', views.ConfirmBook.as_view(), name="ConfirmBook"),
]

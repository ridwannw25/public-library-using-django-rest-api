from django.contrib import admin, messages
from .models import *
from django.utils.translation import ngettext
from django.utils import timezone
# Register your models here.

current_datetime = timezone.now()

admin.site.disable_action("delete_selected")

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_date")
    ordering    = ("title", "author")

@admin.register(BorrowBook)
class BorrowBookAdmin(admin.ModelAdmin):
    list_display = ("username", "title","status_borrow1","borrow_date","category")
    list_filter  = ("borrow_date","id_category__nama_kategori","id_status_books__name_status")

    def category(self, obj):
        kategori = obj.id_category.nama_kategori
        return kategori
    category.short_description = "Category"

    def status_borrow1(self, obj):
        status_brw = obj.id_status_books.name_status
        return status_brw
    status_borrow1.short_description = "Status Borrowed"

@admin.register(ConfirmBorrowBook)
class ConfirmBookBookAdmin(admin.ModelAdmin):
    list_display = ("username", "title", "status")
    actions = ["borrowed","returned"]

    @admin.action(description="Mark selected Confirmed Borrowed")
    def borrowed(self, request, queryset):
        updated = queryset.update(id_status_books="1",borrow_date=current_datetime)
        self.message_user(
            request,
            ngettext(
                "%d successfully marked as confirmed borrowed.",
                "%d successfully marked as confirmed borrowed.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )

    @admin.action(description="Mark selected Confirmed Return")
    def returned(self, request, queryset):
        updated = queryset.update(id_status_books="3",borrow_date=current_datetime)
        self.message_user(
            request,
            ngettext(
                "%d successfully confirmed returned.",
                "%d successfully confirmed returned.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )

    def status(self, obj):
        status_brw = obj.id_status_books.name_status
        return status_brw
    status.short_description = "Status"

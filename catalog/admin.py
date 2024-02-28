from django.contrib import admin
from .models import Book, Video, Game, UserProfile, BorrowRecord

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publisher', 'book_type']

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'director', 'release_year', 'video_type']

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['title', 'platform', 'genre', 'game_type']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'address']


@admin.register(BorrowRecord)
class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ['item', 'borrower', 'borrow_date', 'return_date', 'days_until_return']
    list_filter = ['borrow_date', 'return_date']
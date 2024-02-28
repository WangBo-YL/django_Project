from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Book, BorrowRecord
from .form import BorrowRecordForm
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm


@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BorrowRecordForm(request.POST)
        if form.is_valid():
            borrow_record = form.save(commit=False)
            borrow_record.borrower = request.user.profile
            borrow_record.item = book
            borrow_record.save()
            return redirect('some_success_url')  # point to a new URL
    else:
        form = BorrowRecordForm(initial={'item': book})
    return render(request, 'borrow_book.html', {'form': form, 'book': book})

@login_required
def return_book(request, record_id):
    borrow_record = get_object_or_404(BorrowRecord, pk=record_id)
    if request.method == 'POST':
        borrow_record.return_date = timezone.now()
        borrow_record.save()
        return redirect('some_success_url')  # point to a new URL
    return render(request, 'return_book.html', {'borrow_record': borrow_record})

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
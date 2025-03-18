from django.shortcuts import render, redirect
from .models import Book, Publisher
from .forms import BookForm, PublisherForm

# 출판사 생성
def create_publisher(request):
    if request.method == "POST":
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = PublisherForm()
    return render(request, 'create_publisher.html', {'form': form})

# 책 생성
def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'create_book.html', {'form': form})

# 책 목록 조회
def book_list(request):
    books = Book.objects.select_related('publisher').all()  # 출판사와 조인
    return render(request, 'book_list.html', {'books': books})

# 책 수정
def update_book(request, id):
    book = Book.objects.get(id=id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'update_book.html', {'form': form})

# 책 삭제
def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('book_list')

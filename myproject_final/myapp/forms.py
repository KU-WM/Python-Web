from django import forms
from .models import Publisher, Book

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', 'established_date']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'publisher', 'author', 'published_date']
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),  # 날짜 선택 위젯 추가
        }
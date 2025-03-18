from django import forms
from .models import Book, Publisher

class BookForm(forms.ModelForm):
    publisher = forms.ModelChoiceField(queryset=Publisher.objects.all(), empty_label="Select Publisher")

    class Meta:
        model = Book
        fields = ['title', 'publisher', 'published_date', 'price']

class PublisherForm(forms.ModelForm):

    class Meta:
        model = Publisher
        fields = ['name', 'established_date']


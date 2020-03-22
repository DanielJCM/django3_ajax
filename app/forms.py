# -*- coding: utf-8 -*-
from django import forms
from app.models import *
from django.forms import (
    TextInput, CharField, Select, RadioSelect, Textarea, CheckboxInput
)


class BookForm(forms.ModelForm):
    """
    Form that manages the person model fields
    """

    publication_date = forms.DateTimeInput()

    class Meta:

        model = Book

        fields = ('title', 'publication_date', 'author', 'price', 'pages', 'book_type', )
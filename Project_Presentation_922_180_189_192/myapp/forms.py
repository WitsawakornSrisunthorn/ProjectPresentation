# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# forms.py


class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control mr-sm-2', 'type': 'search', 'placeholder': 'Search', 'aria-label': 'Search'}))

class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('username', 'birth_date', 'password1', 'password2',)
        

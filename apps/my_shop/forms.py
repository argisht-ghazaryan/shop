from django import forms


class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=150, label='Search for Products')

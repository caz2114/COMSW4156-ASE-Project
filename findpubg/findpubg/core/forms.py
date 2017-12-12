from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from findpubg.core.models import Search
from findpubg.core.models import TEAM_CHOICES, REGION_CHOICES
import django_filters
from django_filters import filters


class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('username', 'birth_date', 'password1', 'password2')
        help_texts = {
            'username': 'Required. 150 characters or fewer. Letters, digits and @ . + - _ only',
        }

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = 'Your password must contain at least 9 characters. Your password can\'t be entirely numeric.'

class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ('steam_id', 'team_choices', 'region_choices', 'email', 'rank')

class FilterUser(django_filters.FilterSet):
    rank = django_filters.NumberFilter(name='rank')
    # rank__gt = django_filters.NumberFilter(name='rank', lookup_expr='search__rank__gt')
    # rank__lt = django_filters.NumberFilter(name='rank', lookup_expr='rank__lt')

    class Meta:
        model = Search
        fields = ('steam_id', 'team_choices', 'region_choices','rank')

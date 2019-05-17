from django.forms import ModelForm
from .models import Person
from django import forms

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'foto']

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class TesteForm(forms.Form):
    post = forms.CharField()
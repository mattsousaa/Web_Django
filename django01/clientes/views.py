from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm

def person_list(request):
    # CRUD - Read
    persons = Person.objects.all()
    return render(request, 'person.html', {'persons': persons})


def new_person(request):
    form = PersonForm(request.POST, request.FILES, None)
    # Precisa validar o formulário
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form':form})
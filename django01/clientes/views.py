import pymongo
from pymongo import MongoClient
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Person
from .forms import PersonForm
from .forms import TesteForm
from django.views.generic import TemplateView

# SRV de uso pessoal associada ao e-mail: mateuseng_ec@alu.ufc.br
spi_client = pymongo.MongoClient(
    'mongodb+srv://admin:admin@mylove-jqsvg.gcp.mongodb.net/test?retryWrites=true'
)
cloud_database = spi_client.spi_proj            # Procura no servidor o banco "spi_proj"
cloud_collection = cloud_database.node_track    # Faz consultas nesta label "node_track"

@login_required
def person_list(request):
    # CRUD - Read
    persons = Person.objects.all()
    return render(request, 'person.html', {'persons': persons})

@login_required
def new_person(request):
    form = PersonForm(request.POST, request.FILES or None)
    # Precisa validar o formulário
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form':form})

@login_required
def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form':form})

@login_required
def get_form(request):
    form = TesteForm()
    return render(request, 'name.html', {'form':form})        

@login_required
def get_post(request):
    text = ''
    form = TesteForm(request.POST)
    if form.is_valid():
        text = form.cleaned_data['post']
        form = TesteForm()
    print(text)
    args = {'form':form, 'text':text}
    return render(request, 'name.html', args)

@login_required
def getLastMac(request):
    text = ''
    busca_bd = ''
    form = TesteForm(request.POST)
    if form.is_valid():
        text = form.cleaned_data['post']

    text = text.lower()

    for post in cloud_collection.find({"MAC": text}).sort("TIME"):
        busca_bd = post
    #print(text)
    args = {'form':form, 'text':text, 'busca_bd':busca_bd}
    return render(request, 'get_last_mac.html', args)

@login_required
def getAllMacs(request):
    search_mongo = cloud_collection.find()
    #return HttpResponse('Ola Mundo')
    return render(request, 'get_all_macs.html', {'search_mongo':search_mongo})

@login_required
def getOccurMacs(request):
    text = ''
    busca_bd = ''
    form = TesteForm(request.POST)
    if form.is_valid():
        text = form.cleaned_data['post']
    text = text.lower()
    busca_bd = cloud_collection.find({"MAC": text}).sort("TIME")
   
    args = {'form':form, 'text':text, 'busca_bd':busca_bd}
    return render(request, 'get_occur_macs.html', args)

@login_required
def confirmDelete(request):
    cloud_collection.delete_many({})
    return redirect('person_list')

@login_required
def eraseDataBase(request):
    return render(request, 'delete_bd.html')


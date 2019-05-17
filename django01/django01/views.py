import pymongo
from pymongo import MongoClient
from django.http import HttpResponse
from django.shortcuts import render

# SRV de uso pessoal associada ao e-mail: mateuseng_ec@alu.ufc.br
spi_client = pymongo.MongoClient(
    'mongodb+srv://admin:admin@mylove-jqsvg.gcp.mongodb.net/test?retryWrites=true'
)
cloud_database = spi_client.spi_proj            # Procura no servidor o banco "spi_proj"
cloud_collection = cloud_database.node_track    # Faz consultas nesta label "node_track"

def hello(request):
    #return HttpResponse('Ola Mundo')
    return render(request, 'index.html')

def articles(request, year):
    return  HttpResponse('O ano informado foi: ' + str(year))


def testeSpi(request):
    search_mongo = cloud_collection.find()
    #return HttpResponse('Ola Mundo')
    return render(request, 'spi.html', {'search_mongo':search_mongo})

def lerDoBanco(nome):
    lista_nomes = [
        {'nome': 'Miguel', 'idade': 23},
        {'nome': 'Ana', 'idade': 6},
        {'nome': 'Mateus', 'idade': 41},
        {'nome': 'Luciano', 'idade': 53}
    ]

    for pessoa in lista_nomes:
        if pessoa['nome'] == nome:
            return pessoa
    else:
        return {'nome': 'none', 'idade': 0}


def fnome(request, nome):
    result = lerDoBanco(nome)
    print(nome)
    print(result['idade'])
    if result['idade'] > 0:
        return HttpResponse('A pessoa foi encontrada. Ela tem ' + str(result['idade']) + ' anos')
    else:
        return HttpResponse('Pessoa não encontrada')


def fnome2(request, nome):
    idade = lerDoBanco(nome)['idade']
    return render(request, 'pessoa.html', {'v_idade': idade})
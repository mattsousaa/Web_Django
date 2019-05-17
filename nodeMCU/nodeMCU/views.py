from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    #return HttpResponse('Ola Mundo')
    return render(request, 'index.html')

def articles(request, year):
    return  HttpResponse('O ano informado foi: ' + str(year))

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

def fname2(request, nome):
    idade = lerDoBanco(nome)['idade']
    return render(request, 'pessoa.html', {'v_idade':idade})
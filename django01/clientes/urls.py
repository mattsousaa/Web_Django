from django.urls import path
from django.views import View
from .views import person_list
from .views import new_person
from .views import persons_update
from .views import get_form
from .views import get_post
from .views import getLastMac
from .views import getAllMacs
from .views import getOccurMacs
from .views import eraseDataBase
from .views import confirmDelete

urlpatterns = [
    path('list/', person_list, name='person_list'),
    path('new/', new_person, name='new_person'),
    path('update/<int:id>/', persons_update, name='person_update'),
    path('get_form/', get_form, name=  'get_form'),
    path('get_post/', get_post, name=  'get_post'),
    path('getLastMac/', getLastMac, name=  'getLastMac'),
    path('getAllMacs/', getAllMacs, name=  'getAllMacs'),
    path('getOccurMacs/', getOccurMacs, name=  'getOccurMacs'),
    path('confirmDelete/', confirmDelete, name=  'confirmDelete'),
    path('eraseDataBase/', eraseDataBase, name=  'eraseDataBase'),
] 

from django.urls import path
from .views import person_list
from .views import new_person

urlpatterns = [
    path('list/', person_list, name='person_list'),
    path('new/', new_person, name='new_person'),
] 

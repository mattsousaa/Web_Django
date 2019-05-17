from django.contrib import admin
from django.urls import path, include
from .views import hello
from .views import articles
from .views import fnome
from .views import fnome2
from .views import testeSpi
from django.conf import settings
from django.conf.urls.static import static
from clientes import urls as clients_urls
from django.contrib.auth import views as auth_views
from home import urls as home_urls

urlpatterns = [
    path('', include(home_urls)),
    path('hello/', hello),
    path('login/', auth_views.LoginView.as_view(), name='login'), # Importa view de login do Django 
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'), # Importa view de logout do Django
    path('admin/', admin.site.urls),
    path('articles/<int:year>/', articles),
    path('ler_bd/', testeSpi),
    path('person/', include(clients_urls)),
    path('pessoa/<str:nome>/', fnome),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

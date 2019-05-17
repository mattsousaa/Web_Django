from django.contrib import admin
from django.urls import path, include
from .views import hello
from .views import articles
from .views import fnome
from .views import fname2
from django.conf import settings
from django.conf.urls.static import static
from NodeTrack import urls as clients_urls

urlpatterns = [
    path('hello/', hello),
    path('admin/', admin.site.urls),
    path('articles/<int:year>/', articles),
    #path('pessoa/<str:nome>/', fnome),
    path('pessoa/<str:nome>/', fname2),
    path('person/', include(clients_urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

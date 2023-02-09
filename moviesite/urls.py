from django.contrib import admin
from django.urls import path

from movie.views import *
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movie.urls')),
]

handler404=pageNotFound
# handler403=pageForbidden
# handler400=pageBadrequest
# handler500=pageInternalServerError

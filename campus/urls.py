from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView
from django.urls import path

urlpatterns = [


    path('admin/', admin.site.urls),

    # sua URL raiz
    path('', RedirectView.as_view(url='/admin/', permanent=False)),
]

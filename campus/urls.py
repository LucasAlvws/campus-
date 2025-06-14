from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # sua URL raiz
    path('', RedirectView.as_view(url='/admin/', permanent=False)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

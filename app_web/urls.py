
from django.contrib import admin
from django.urls import path
from core.views import home, CrieteViewEntregador
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('enviando-email/' , send_email_mrbee, name='send'),
    path('cadastro/', 
        CrieteViewEntregador.as_view(), 
        name='create_entregador'
    ),
    path('', home, name='home')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

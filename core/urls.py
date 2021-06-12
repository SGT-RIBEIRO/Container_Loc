from django.urls import path
from .views import IndexView, SobreNosView, ContatoView, ProdutoView, ContainerView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    path('', IndexView.as_view(), name='index'),
    path('sobre_nos/', SobreNosView.as_view(), name='sobre_nos'),
    path('contato/', ContatoView.as_view(), name='contato'),
    path('produtos/', ProdutoView.as_view(), name='produtos'),
    path('container/', ContainerView.as_view(), name='container'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
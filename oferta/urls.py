from django.urls import path
from .views import home, dashboard, login_view, logout_view, register_view, criar_oferta, editar_oferta, remover_oferta, detalhes_oferta

urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('criar_oferta/', criar_oferta, name='criar_oferta'),
    path('oferta/editar/<int:id>/', editar_oferta, name='editar_oferta'),
    path('oferta/remover/<int:id>/', remover_oferta, name='remover_oferta'),
    path('detalhes_oferta/<int:id>/', detalhes_oferta, name='detalhes_oferta'),
]

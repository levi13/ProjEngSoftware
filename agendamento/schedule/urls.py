# schedule/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('agendamento/novo/', views.agendamento_create, name='agendamento_create'),
    path('', views.agendamentos_list, name='agendamentos_list'),
    path('<int:id>/editar/', views.agendamento_edit, name='agendamento_edit'),
    path('<int:id>/deletar/', views.agendamento_delete, name='agendamento_delete'),
]

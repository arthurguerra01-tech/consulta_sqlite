from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastro_paciente, name='cadastro'),
    path('agendar/<int:paciente_id>/', views.agendar_consulta, name='agendar'),
    path('minhas-consultas/<int:paciente_id>/', views.minhas_consultas, name='minhas_consultas'),
    path('excluir/<int:consulta_id>/<int:paciente_id>/', views.excluir_consulta, name='excluir_consulta'),
]

from django.shortcuts import render, redirect
from .models import Medico, Paciente, Consulta

def cadastro_paciente(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        cpf = request.POST['cpf']
        paciente, created = Paciente.objects.get_or_create(nome=nome, cpf=cpf)
        return redirect('agendar', paciente_id=paciente.id)
    return render(request, 'clinica/cadastro.html')

def agendar_consulta(request, paciente_id):
    paciente = Paciente.objects.get(id=paciente_id)
    medicos = Medico.objects.all()
    if request.method == 'POST':
        medico_id = request.POST['medico']
        medico = Medico.objects.get(id=medico_id)
        Consulta.objects.create(paciente=paciente, medico=medico)
        return redirect('minhas_consultas', paciente_id=paciente.id)
    return render(request, 'clinica/agendar.html', {'medicos': medicos, 'paciente': paciente})

def minhas_consultas(request, paciente_id):
    paciente = Paciente.objects.get(id=paciente_id)
    consultas = Consulta.objects.filter(paciente=paciente)
    return render(request, 'clinica/minhas_consultas.html', {'consultas': consultas, 'paciente': paciente})

def excluir_consulta(request, consulta_id, paciente_id):
    consulta = Consulta.objects.get(id=consulta_id)
    consulta.delete()
    return redirect('minhas_consultas', paciente_id=paciente_id)

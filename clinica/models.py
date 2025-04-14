from django.db import models

class Medico(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    data_atendimento = models.DateField()

    def __str__(self):
        return f"{self.nome} - {self.especialidade}"

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.nome

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)

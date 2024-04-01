from datetime import date
from django.db import models
from django.contrib.auth.models import User

class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # associar User do sistema
    nome = models.CharField(max_length=128, blank=False)
    cpf = models.CharField(max_length=11, blank=False)
    email = models.CharField(max_length=128, blank=True)
    endereco = models.CharField(max_length=128, blank=True)
    telefone = models.CharField(max_length=22, blank=False)

    class Meta:
        db_table = 'professor'

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    class Escolaridade(models.TextChoices):
        ANF = 'ANF', 'Analfabeto'
        EDB = 'EDB', 'Educação Básica'
        EFC = 'EFC', 'Ensino Fundamental Completo'
        EMI = 'EMI', 'Ensino Medio Incompleto'
        EMC = 'EMC', 'Ensino Medio Completo'
        ESC = 'ESC', 'Ensino Superior Completo'

    class CondicaoFinanceira(models.TextChoices):
        B = 'B', 'Baixa'
        M = 'M', 'Média'
        A = 'A', 'Alta'

    id_aluno = models.AutoField(primary_key=True, unique=True)
    nome = models.CharField(max_length=128, blank=False)
    cpf = models.CharField(max_length=11, blank=False)
    email = models.EmailField(max_length=128, blank=False)
    endereco = models.CharField(max_length=128, blank=True)
    telefone = models.CharField(max_length=22, blank=False)
    condicao_financeira = models.CharField(max_length=1, choices=CondicaoFinanceira.choices, null=True)
    escolaridade = models.CharField(max_length=3, choices=Escolaridade.choices, null=True)
    trabalha =  models.BooleanField(null=False)

    class Meta:
        db_table = 'aluno'

    def __str__(self):
        return self.nome


class Curso(models.Model):
    nome = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'curso'

    def __str__(self):
        return self.nome
    

class Disciplina(models.Model):
    nome = models.CharField(max_length=50)
    cursos = models.ManyToManyField(Curso, db_table='disciplina_curso')

    class Meta:
        db_table = 'disciplina'

    def __str__(self):
        return self.nome


class Turma(models.Model):
    periodo = models.IntegerField(null=False)
    ano = models.IntegerField(null=False)
    qtd_vagas = models.IntegerField(null=True)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    alunos = models.ManyToManyField(Aluno, db_table='turma_aluno')

    class Meta:
        db_table = 'turma'

    def __str__(self):
        detalhe = '%s - %d° Periodo' % (self.disciplina, self.periodo)
        return detalhe
    
    
class Aula(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    data = models.DateField(auto_now=False, auto_now_add=False, null=False, default=date.today)

    class Meta:
        db_table = 'aula'

    def __str__(self):
        detalhe = '%s - %s' % (self.turma, self.data)
        return detalhe
    

class Presenca(models.Model):
    presente = models.BooleanField()
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE, unique=False)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, unique=False)

    class Meta:
        db_table = 'presenca'

    def __str__(self):
        detalhe = '%s - %s' % (self.aluno, self.aula)
        return detalhe


class Matricula(models.Model):
    aluno = models.OneToOneField(Aluno, on_delete=models.CASCADE)
    data = models.DateField(auto_now=False, auto_now_add=False, null=False, default=date.today)
    desistencia = models.BooleanField(default=False)

    class Meta:
        db_table = 'matricula'


from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import FileExtensionValidator

# TODA A CLASSE DE MODELOS QUE SEGUE OS DIAGRMAS DE CLASSE E DE BANCO DE DADOS
class Course(models.Model):
    code = models.CharField("Código", max_length=10, unique=True)
    name = models.CharField("Nome", max_length=100)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self):
        return f"{self.name} ({self.code})"

class User(AbstractUser):
    course = models.ForeignKey(
        Course,
        verbose_name="Curso",
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    registration_number = models.CharField("Matrícula", max_length=20, blank=True, null=True)
    role = models.CharField(
        "Cargo",
        max_length=20,
        choices=[('student', 'Aluno'), ('coordinator', 'Coordenador'), ('dce', 'DCE')],
        default='student'
    )

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

class Document(models.Model):
    TYPES = [
        ('transcript', 'Histórico Escolar'),
        ('enrollment', 'Comprovante de Matrícula'),
        ('syllabus', 'Programa de Disciplina'),
    ]

    STATUSES = [
        ('pending', 'Pendente'),
        ('in_progress', 'Em andamento'),
        ('completed', 'Concluído'),
        ('denied', 'Negado'),
    ]

    doc_type = models.CharField("Tipo de Documento", max_length=50, choices=TYPES)
    reason = models.TextField("Motivo")
    status = models.CharField("Status", max_length=20, choices=STATUSES, default='pending')
    request_date = models.DateTimeField("Data da Solicitação", auto_now_add=True)
    estimated_date = models.DateField("Data Estimada de Entrega", null=True, blank=True)
    requester = models.ForeignKey(User, verbose_name="Solicitante", on_delete=models.CASCADE)
    file = models.FileField(
        "Arquivo do Documento",
        upload_to="documentos/",
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
        help_text="Somente arquivos .pdf"
    )
    class Meta:
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"

class AcademicInfo(models.Model):
    user = models.ForeignKey(User, verbose_name="Usuário", on_delete=models.CASCADE)
    subject = models.CharField("Disciplina", max_length=100)
    status = models.CharField("Status", max_length=20)
    term = models.CharField("Período", max_length=10)

    class Meta:
        verbose_name = "Informação Acadêmica"
        verbose_name_plural = "Informações Acadêmicas"

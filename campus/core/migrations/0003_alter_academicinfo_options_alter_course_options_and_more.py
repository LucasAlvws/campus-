# Generated by Django 5.2.2 on 2025-06-14 13:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_course_alter_user_course'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='academicinfo',
            options={'verbose_name': 'Informação Acadêmica', 'verbose_name_plural': 'Informações Acadêmicas'},
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'Curso', 'verbose_name_plural': 'Cursos'},
        ),
        migrations.AlterModelOptions(
            name='document',
            options={'verbose_name': 'Documento', 'verbose_name_plural': 'Documentos'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Usuário', 'verbose_name_plural': 'Usuários'},
        ),
        migrations.AlterField(
            model_name='academicinfo',
            name='status',
            field=models.CharField(max_length=20, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='academicinfo',
            name='subject',
            field=models.CharField(max_length=100, verbose_name='Disciplina'),
        ),
        migrations.AlterField(
            model_name='academicinfo',
            name='term',
            field=models.CharField(max_length=10, verbose_name='Período'),
        ),
        migrations.AlterField(
            model_name='academicinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
        migrations.AlterField(
            model_name='course',
            name='code',
            field=models.CharField(max_length=10, unique=True, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='document',
            name='doc_type',
            field=models.CharField(choices=[('transcript', 'Histórico Escolar'), ('enrollment', 'Comprovante de Matrícula'), ('syllabus', 'Programa de Disciplina')], max_length=50, verbose_name='Tipo de Documento'),
        ),
        migrations.AlterField(
            model_name='document',
            name='estimated_date',
            field=models.DateField(blank=True, null=True, verbose_name='Data Estimada de Entrega'),
        ),
        migrations.AlterField(
            model_name='document',
            name='reason',
            field=models.TextField(verbose_name='Motivo'),
        ),
        migrations.AlterField(
            model_name='document',
            name='request_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data da Solicitação'),
        ),
        migrations.AlterField(
            model_name='document',
            name='requester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Solicitante'),
        ),
        migrations.AlterField(
            model_name='document',
            name='status',
            field=models.CharField(default='Pendente', max_length=20, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='user',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.course', verbose_name='Curso'),
        ),
        migrations.AlterField(
            model_name='user',
            name='registration_number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Matrícula'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('student', 'Aluno'), ('coordinator', 'Coordenador'), ('dce', 'DCE')], default='student', max_length=20, verbose_name='Cargo'),
        ),
    ]

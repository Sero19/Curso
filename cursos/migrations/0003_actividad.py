# Generated by Django 4.0.5 on 2022-07-01 13:06

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0002_alter_cursos_options_cursos_imagen_alter_cursos_link_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Clave de Actividad')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Registrado')),
                ('descripCurso', ckeditor.fields.RichTextField(verbose_name='Descripcion del Curso')),
                ('nombreCurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.cursos', verbose_name='Curso')),
            ],
            options={
                'verbose_name': 'Actividad',
                'verbose_name_plural': 'Actividades',
                'ordering': ['-created'],
            },
        ),
    ]
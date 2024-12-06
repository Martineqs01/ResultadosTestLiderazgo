# Generated by Django 5.1.3 on 2024-11-19 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('sexo', models.CharField(max_length=50)),
                ('localidad', models.CharField(max_length=255)),
                ('correo_electronico', models.EmailField(max_length=254)),
                ('institucion_educativa', models.CharField(max_length=255)),
                ('programa_educativo', models.CharField(max_length=255)),
                ('semestre', models.CharField(max_length=50)),
                ('liderazgo_kurt_lewin', models.CharField(max_length=50)),
                ('liderazgo_daniel_goleman', models.CharField(max_length=50)),
            ],
        ),
    ]

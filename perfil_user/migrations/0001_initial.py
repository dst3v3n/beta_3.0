# Generated by Django 5.0.3 on 2024-03-21 06:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('HojaVida', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Profesion', models.CharField(blank=True, max_length=100, null=True)),
                ('Cargo', models.CharField(blank=True, max_length=100, null=True)),
                ('Ubicacion', models.CharField(blank=True, max_length=100, null=True)),
                ('Fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('Registro', models.DateTimeField(auto_now_add=True)),
                ('Redes_sociales', models.URLField(blank=True, null=True)),
                ('Fondo', models.ImageField(blank=True, null=True, upload_to='fondos/')),
                ('Foto_perfil', models.ImageField(blank=True, null=True, upload_to='fotos/')),
                ('id_direc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HojaVida.personal_information')),
                ('id_myuser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfiles',
                'db_table': 'Perfil',
            },
        ),
    ]

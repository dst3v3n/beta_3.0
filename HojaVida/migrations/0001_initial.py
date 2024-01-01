# Generated by Django 4.1.13 on 2023-12-31 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Additional_information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('information_adi', models.TextField()),
                ('id_myuser', models.PositiveIntegerField(null=True, unique=True)),
            ],
            options={
                'verbose_name': 'additional_information',
                'verbose_name_plural': 'additional_information',
                'db_table': 'additional_information',
            },
        ),
        migrations.CreateModel(
            name='Business_references',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=50)),
                ('boss_name', models.CharField(blank=True, max_length=50)),
                ('address_company', models.CharField(blank=True, max_length=50)),
                ('cell_number_busi', models.CharField(blank=True, max_length=11)),
                ('id_myuser', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'business_references',
                'verbose_name_plural': 'business_references',
                'db_table': 'business_references',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archive', models.FileField(upload_to='Archivo_Educacion')),
                ('name_institution', models.CharField(max_length=50)),
                ('graduation_year', models.DateField()),
                ('time', models.IntegerField()),
                ('id_myuser', models.PositiveIntegerField(null=True)),
            ],
            options={
                'verbose_name': 'Education',
                'verbose_name_plural': 'Educations',
                'db_table': 'Education',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('company_position', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('functions', models.TextField(blank=True, null=True)),
                ('id_myuser', models.PositiveIntegerField(null=True)),
            ],
            options={
                'verbose_name': 'Experience',
                'verbose_name_plural': 'Experiences',
                'db_table': 'Experience',
            },
        ),
        migrations.CreateModel(
            name='Personal_information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('cell_phone', models.CharField(max_length=11)),
                ('date', models.DateField()),
                ('type_d', models.CharField(choices=[('Cedula Ciudadania', 'Cedula Ciudadania'), ('Cedula Extranjera', 'Cedula Extranjera'), ('Pasaporte', 'Pasaporte'), ('Tarjeta Identidad', 'Tarjeta Identidad')], default='Cedula Ciudadania', max_length=50)),
                ('n_document', models.CharField(max_length=15)),
                ('gender', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Otro', 'Otro')], default='Masculino', max_length=50)),
                ('age', models.IntegerField()),
                ('civil', models.CharField(choices=[('Casado', 'Casado'), ('Union libre', 'Union libre'), ('Soltero', 'Soltero')], default='Soltero', max_length=50)),
                ('id_myuser', models.PositiveIntegerField(null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Personal_information',
                'verbose_name_plural': 'Personal_information',
                'db_table': 'Personal_information',
            },
        ),
        migrations.CreateModel(
            name='Personal_references',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=50)),
                ('last_person_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('cell_number', models.CharField(max_length=11)),
                ('id_myuser', models.PositiveIntegerField(null=True)),
            ],
            options={
                'verbose_name': 'personal_references',
                'verbose_name_plural': 'personal_references',
                'db_table': 'personal_references',
            },
        ),
    ]
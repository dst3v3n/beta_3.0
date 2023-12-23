# Generated by Django 4.1.13 on 2023-12-23 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_myuser', models.PositiveIntegerField(unique=True)),
                ('nit', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'companies',
                'db_table': 'Company',
            },
        ),
    ]
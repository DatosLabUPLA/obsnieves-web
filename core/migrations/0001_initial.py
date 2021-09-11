# Generated by Django 3.2.7 on 2021-09-11 03:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre del cargo')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Descripción')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='creado')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='modificado')),
            ],
            options={
                'verbose_name': 'cargo',
                'verbose_name_plural': 'cargos',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/team/', verbose_name='Imagen')),
                ('index', models.PositiveSmallIntegerField(default=0, help_text='Este campo se utiliza para dar orden de preferencia de aparición. Evitar modificar.', verbose_name='Indice')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='creado')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='modificado')),
                ('id_position', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='core.position', verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'equipo',
                'verbose_name_plural': 'equipos',
                'ordering': ['-created'],
            },
        ),
    ]
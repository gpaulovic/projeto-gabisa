# Generated by Django 5.0.1 on 2024-02-02 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=15)),
                ('endereco', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=14, unique=True)),
            ],
        ),
    ]

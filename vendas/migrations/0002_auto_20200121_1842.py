# Generated by Django 3.0.2 on 2020-01-21 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venda',
            old_name='deconto',
            new_name='desconto',
        ),
    ]
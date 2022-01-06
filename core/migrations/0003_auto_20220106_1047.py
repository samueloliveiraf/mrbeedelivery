# Generated by Django 3.2.9 on 2022-01-06 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20220106_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='entregadore',
            name='endereco',
            field=models.CharField(default=1, max_length=200, verbose_name='Endereço'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entregadore',
            name='telefone',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=14),
            preserve_default=False,
        ),
    ]

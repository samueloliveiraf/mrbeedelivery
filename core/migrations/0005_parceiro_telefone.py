# Generated by Django 3.2.9 on 2022-02-13 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_parceiro_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='parceiro',
            name='telefone',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=14),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2.7 on 2021-09-19 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_store'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='type',
            field=models.CharField(choices=[('Abarrotes', 'Abarrotes'), ('Auttoservicio', 'Autoservicio')], default='Autoservicio', max_length=15, verbose_name='Tipo de tienda'),
        ),
    ]

# Generated by Django 3.2.9 on 2021-11-26 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='americancrew',
            name='availibility',
            field=models.CharField(max_length=20, null=True, verbose_name='Наличие'),
        ),
        migrations.AddField(
            model_name='philipmartins',
            name='availibility',
            field=models.CharField(max_length=20, null=True, verbose_name='Наличие'),
        ),
    ]

# Generated by Django 4.1.7 on 2023-02-21 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_hogool', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='land',
            name='avalability',
            field=models.BooleanField(),
        ),
    ]

# Generated by Django 4.1.7 on 2023-02-22 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_hogool', '0002_alter_land_avalability'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investorinfo',
            name='experince',
        ),
    ]

# Generated by Django 3.1.3 on 2020-11-06 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20201106_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='apellidos',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]

# Generated by Django 3.1.3 on 2020-11-06 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201103_0509'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='age',
            field=models.CharField(blank=True, max_length=3),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]

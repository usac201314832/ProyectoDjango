# Generated by Django 3.1.3 on 2020-11-08 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_userprofile_mascotas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='apellidos',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='edad',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mascotas',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]

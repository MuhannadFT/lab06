# Generated by Django 5.0.1 on 2024-04-20 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='code',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
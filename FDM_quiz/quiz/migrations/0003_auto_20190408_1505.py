# Generated by Django 2.1.7 on 2019-04-08 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_userscore'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userscore',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]

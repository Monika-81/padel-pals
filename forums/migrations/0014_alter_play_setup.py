# Generated by Django 3.2.13 on 2022-06-11 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0013_delete_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='play',
            name='setup',
            field=models.CharField(choices=[('Searching for a Player', 'Player'), ('Searching for a Team', 'Team')], max_length=100),
        ),
    ]

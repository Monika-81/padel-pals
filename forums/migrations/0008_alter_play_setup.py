# Generated by Django 3.2.13 on 2022-06-10 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0007_alter_play_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='play',
            name='setup',
            field=models.CharField(choices=[('Searching for a player', 'Player'), ('Searching for a team', 'Team')], max_length=100),
        ),
    ]
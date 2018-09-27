# Generated by Django 2.1 on 2018-08-26 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0002_game_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='status',
            field=models.CharField(choices=[('F', 'First Player to Move'), ('S', 'Second Player To Move'), ('W', 'First Player To Wins'), ('L', 'Second Player To Wins'), ('D', 'Draw')], default='F', max_length=1),
        ),
    ]
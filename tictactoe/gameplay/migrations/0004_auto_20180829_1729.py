# Generated by Django 2.1 on 2018-08-29 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0003_auto_20180826_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='move',
            name='by_first_player',
            field=models.BooleanField(editable=False),
        ),
    ]

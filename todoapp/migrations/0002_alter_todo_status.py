# Generated by Django 4.0.6 on 2022-07-20 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.IntegerField(choices=[(0, 'New'), (1, 'Process'), (2, 'Complated'), (3, 'Cancelled')], default=0),
        ),
    ]

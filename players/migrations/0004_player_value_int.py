# Generated by Django 2.2 on 2019-09-27 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0003_auto_20190922_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='value_int',
            field=models.IntegerField(default=0),
        ),
    ]

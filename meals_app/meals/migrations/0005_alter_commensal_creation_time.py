# Generated by Django 4.0.1 on 2022-02-04 08:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0004_alter_commensal_creation_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commensal',
            name='creation_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 4, 9, 38, 36, 663487), verbose_name='creation time'),
        ),
    ]
# Generated by Django 4.1.4 on 2022-12-08 03:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("principal", "0002_alter_profile_f_fin_alter_profile_f_inicio"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 12, 7, 22, 7, 48, 255117)
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="f_fin",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 1, 6, 22, 7, 48, 255117)
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="f_inicio",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 12, 7, 22, 7, 48, 255117)
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="updated",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 12, 7, 22, 7, 48, 255117)
            ),
        ),
    ]
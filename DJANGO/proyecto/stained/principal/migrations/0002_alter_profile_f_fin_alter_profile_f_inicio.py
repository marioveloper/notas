# Generated by Django 4.1.4 on 2022-12-08 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("principal", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="f_fin",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="f_inicio",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
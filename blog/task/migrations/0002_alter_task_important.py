# Generated by Django 4.2.5 on 2023-09-22 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='important',
            field=models.BooleanField(default=True),
        ),
    ]

# Generated by Django 4.1.1 on 2022-10-12 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_mechanicservice_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='mechanicservice',
            name='hour',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='mechanicservice',
            name='date',
            field=models.DateField(null=True),
        ),
    ]

# Generated by Django 4.1 on 2023-03-30 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssr', '0003_alter_vehicle_details_veh_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='is_available',
            field=models.IntegerField(default=False, null=True),
        ),
    ]

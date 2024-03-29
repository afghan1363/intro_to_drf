# Generated by Django 5.0 on 2024-01-03 10:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0003_milage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='milage',
            name='car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='milage', to='vehicle.car'),
        ),
        migrations.AlterField(
            model_name='milage',
            name='moto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='milage', to='vehicle.moto'),
        ),
    ]

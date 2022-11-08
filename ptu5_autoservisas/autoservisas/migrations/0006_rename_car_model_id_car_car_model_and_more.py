# Generated by Django 4.1.3 on 2022-11-07 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('autoservisas', '0005_orderline'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='car_model_id',
            new_name='car_model',
        ),
        migrations.RemoveField(
            model_name='order',
            name='car_id',
        ),
        migrations.AddField(
            model_name='order',
            name='car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservisas.car'),
        ),
    ]
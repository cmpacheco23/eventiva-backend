# Generated by Django 4.2.6 on 2024-01-11 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.CharField(choices=[('Trip', 'Trip'), ('Activity', 'Activity')], default='Trip', max_length=20),
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='event',
            name='endDate',
            field=models.DateField(default='2024-01-12 22:47:16.864697+00:00', verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='event',
            name='startDate',
            field=models.DateField(default='<function now at 0x1055ad160>', verbose_name='Start Date'),
        ),
        migrations.CreateModel(
            name='Trips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapi.event')),
            ],
        ),
    ]

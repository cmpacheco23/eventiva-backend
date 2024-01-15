# Generated by Django 4.2.6 on 2024-01-15 20:07

from django.db import migrations, models
import django.db.models.deletion
from datetime import datetime, timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_event_event_type_event_location_alter_event_enddate_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('user_id', models.CharField(max_length=36, primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.RemoveField(
            model_name='event',
            name='endDate',
        ),
        migrations.RemoveField(
            model_name='event',
            name='startDate',
        ),
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(default='Your default description here'),
        ),
        migrations.AddField(
            model_name='event',
            name='end_date',
            field=models.DateField(default=datetime(2024, 1, 16, 20, 7, 28, 866718, tzinfo=timezone.utc), verbose_name='End Date'),
        ),
        migrations.AddField(
            model_name='event',
            name='start_date',
            field=models.DateField(default=datetime(2024, 1, 15, 20, 7, 28, 866718, tzinfo=timezone.utc), verbose_name='Start Date'),
        ),
        migrations.AlterField(
            model_name='trips',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapi.event'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='profile_avatars/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('app_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapi.appuser')),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('duration', models.CharField(choices=[('12hrs', '12 hours'), ('24hrs', '24 hours'), ('48hrs', '48 hours'), ('72hrs', '72 hours')], max_length=10)),
                ('poll_result', models.CharField(max_length=255)),
                ('option1', models.CharField(blank=True, max_length=255, null=True)),
                ('option2', models.CharField(blank=True, max_length=255, null=True)),
                ('option3', models.CharField(blank=True, max_length=255, null=True)),
                ('option4', models.CharField(blank=True, max_length=255, null=True)),
                ('option5', models.CharField(blank=True, max_length=255, null=True)),
                ('option6', models.CharField(blank=True, max_length=255, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='polls', to='myapi.event')),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapi.profile')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='event_owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myapi.profile'),
        ),
        migrations.AddField(
            model_name='trips',
            name='profile',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='myapi.profile'),
        ),
    ]

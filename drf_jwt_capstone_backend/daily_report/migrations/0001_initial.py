# Generated by Django 3.2.8 on 2021-12-03 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('officer_id', models.IntegerField(blank=True, default=0)),
                ('date', models.DateTimeField()),
                ('calls_for_service', models.IntegerField(blank=True, default=0)),
                ('reports', models.IntegerField(blank=True, default=0)),
                ('supplements', models.IntegerField(blank=True, default=0)),
                ('citations_issued', models.IntegerField(blank=True, default=0)),
                ('warnings_issued', models.IntegerField(blank=True, default=0)),
                ('traffic_stops', models.IntegerField(blank=True, default=0)),
                ('citizen_contacts', models.IntegerField(blank=True, default=0)),
                ('juvenile_contacts', models.IntegerField(blank=True, default=0)),
                ('assigned_area', models.CharField(blank=True, max_length=30)),
                ('assigned_vehicle', models.IntegerField(blank=True, default=0)),
                ('miles_driven', models.IntegerField(blank=True, default=0)),
                ('hours_worked', models.IntegerField(blank=True, default=0)),
                ('case_numbers', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
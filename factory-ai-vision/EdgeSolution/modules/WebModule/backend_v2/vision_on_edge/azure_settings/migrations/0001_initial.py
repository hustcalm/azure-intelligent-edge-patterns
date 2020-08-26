# Generated by Django 3.0.8 on 2020-08-26 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100, unique=True)),
                ('endpoint', models.CharField(blank=True, max_length=1000)),
                ('training_key', models.CharField(blank=True, max_length=1000)),
                ('iot_hub_connection_string', models.CharField(blank=True, max_length=1000)),
                ('device_id', models.CharField(blank=True, max_length=1000)),
                ('module_id', models.CharField(blank=True, max_length=1000)),
                ('is_collect_data', models.BooleanField(default=False)),
                ('is_trainer_valid', models.BooleanField(default=False)),
                ('obj_detection_domain_id', models.CharField(blank=True, default='', max_length=1000)),
                ('app_insight_has_init', models.BooleanField(default=False)),
            ],
            options={
                'unique_together': {('endpoint', 'training_key')},
            },
        ),
    ]

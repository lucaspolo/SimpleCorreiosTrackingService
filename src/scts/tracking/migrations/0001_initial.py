# Generated by Django 2.2.4 on 2019-09-22 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrackingCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'tracking',
                'managed': True,
            },
        ),
    ]

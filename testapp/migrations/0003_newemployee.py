# Generated by Django 4.0 on 2022-01-15 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_testapp_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='newEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.IntegerField()),
                ('ename', models.CharField(max_length=30)),
                ('bdate', models.CharField(max_length=15)),
                ('eaddress', models.CharField(max_length=150)),
                ('estate', models.CharField(max_length=40)),
                ('enum', models.IntegerField()),
                ('erole', models.CharField(max_length=25)),
                ('esal', models.FloatField()),
                ('ejoin', models.CharField(max_length=20)),
            ],
        ),
    ]

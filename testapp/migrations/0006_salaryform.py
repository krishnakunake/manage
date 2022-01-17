# Generated by Django 4.0 on 2022-01-16 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_delete_salaryform'),
    ]

    operations = [
        migrations.CreateModel(
            name='salaryForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.IntegerField()),
                ('ename', models.CharField(max_length=30)),
                ('emonth', models.CharField(max_length=15)),
                ('edate', models.CharField(max_length=150)),
                ('erole', models.CharField(max_length=40)),
                ('ebasic', models.FloatField()),
                ('epf', models.FloatField()),
                ('eadvance', models.FloatField()),
                ('enet', models.FloatField()),
            ],
        ),
    ]
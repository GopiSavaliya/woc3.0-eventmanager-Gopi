# Generated by Django 3.1.5 on 2021-01-19 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('ContactNo', models.CharField(max_length=10)),
                ('Email', models.CharField(max_length=255)),
                ('EventName', models.CharField(max_length=50)),
                ('RegType', models.CharField(max_length=15)),
                ('NoOfPeople', models.IntegerField()),
            ],
        ),
    ]
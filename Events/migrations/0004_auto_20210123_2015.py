# Generated by Django 3.1.5 on 2021-01-23 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0003_auto_20210123_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='EventPoster',
            field=models.ImageField(upload_to='EventPoster'),
        ),
    ]

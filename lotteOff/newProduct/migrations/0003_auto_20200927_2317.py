# Generated by Django 3.1.1 on 2020-09-27 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newProduct', '0002_apply'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='date_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='apply',
            name='store_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

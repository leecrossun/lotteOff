# Generated by Django 3.1.1 on 2020-10-03 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DriveThru',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop', models.CharField(max_length=20)),
                ('items', models.TextField()),
                ('state', models.IntegerField(default=0)),
                ('pick_date', models.DateTimeField()),
                ('pub_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

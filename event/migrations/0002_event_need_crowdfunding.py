# Generated by Django 3.2.5 on 2022-03-12 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='need_crowdfunding',
            field=models.BooleanField(default=False),
        ),
    ]

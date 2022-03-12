# Generated by Django 3.2.5 on 2022-03-12 11:39

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('event', '0002_event_need_crowdfunding'),
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('age', models.IntegerField()),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('available_at', models.CharField(choices=[('From 7 AM', 'From 7 AM'), ('From 8 AM', 'From 8 AM'), ('From 9 AM', 'From 9 AM'), ('From 10 AM', 'From 10 AM'), ('From 11 AM', 'From 11 AM'), ('From 12 Noon', 'From 12 Noon'), ('From 1 PM', 'From 1 PM'), ('From 2 PM', 'From 2 PM'), ('From 3 PM', 'From 3 PM'), ('From 4 PM', 'From 4 PM'), ('From 5 PM', 'From 5 PM'), ('From 6 PM', 'From 6 PM')], max_length=250)),
                ('is_selected', models.BooleanField(default=False)),
                ('aadhar_image', models.ImageField(upload_to='Aadhar/')),
                ('event_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event')),
            ],
        ),
    ]

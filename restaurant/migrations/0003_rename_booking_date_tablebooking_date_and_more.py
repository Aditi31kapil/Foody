# Generated by Django 5.0.4 on 2024-06-14 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_remove_tablebooking_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tablebooking',
            old_name='booking_date',
            new_name='Date',
        ),
        migrations.RenameField(
            model_name='tablebooking',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='tablebooking',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='tablebooking',
            old_name='phone_number',
            new_name='Number',
        ),
        migrations.RenameField(
            model_name='tablebooking',
            old_name='persons',
            new_name='Person',
        ),
    ]

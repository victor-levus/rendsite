# Generated by Django 4.1.4 on 2023-03-23 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('betcodes', '0003_bookcodeinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookcodeinfo',
            old_name='ticket_time',
            new_name='ticket_date',
        ),
    ]
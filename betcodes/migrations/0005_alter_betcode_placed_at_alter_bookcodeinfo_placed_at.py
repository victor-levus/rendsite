# Generated by Django 4.2.3 on 2023-07-13 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('betcodes', '0004_rename_ticket_time_bookcodeinfo_ticket_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='betcode',
            name='placed_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='bookcodeinfo',
            name='placed_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

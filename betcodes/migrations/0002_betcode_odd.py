# Generated by Django 4.1.4 on 2023-03-21 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('betcodes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='betcode',
            name='odd',
            field=models.DecimalField(decimal_places=2, default=1.34, max_digits=6),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2 on 2023-04-13 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_remove_band_year_formed'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='year_formed',
            field=models.IntegerField(default=2000),
            preserve_default=False,
        ),
    ]

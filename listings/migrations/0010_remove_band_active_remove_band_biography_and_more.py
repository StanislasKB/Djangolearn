# Generated by Django 4.2 on 2023-04-13 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0009_rename_year_formed_band_year_forme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='active',
        ),
        migrations.RemoveField(
            model_name='band',
            name='biography',
        ),
        migrations.RemoveField(
            model_name='band',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='band',
            name='official_homepage',
        ),
        migrations.RemoveField(
            model_name='band',
            name='year_forme',
        ),
        migrations.AddField(
            model_name='listing',
            name='description',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='sold',
            field=models.IntegerField(default=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='types',
            field=models.CharField(choices=[('Records', 'Disque'), ('Posters', 'Affiche'), ('Clothes', 'Habit'), ('Miscellanous', 'Divers')], default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='year',
            field=models.IntegerField(default=2005),
            preserve_default=False,
        ),
    ]

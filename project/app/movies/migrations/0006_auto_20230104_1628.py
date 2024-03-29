# Generated by Django 3.2.13 on 2023-01-04 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20221222_2121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='directorfilmwork',
            name='director',
        ),
        migrations.RemoveField(
            model_name='directorfilmwork',
            name='film_work',
        ),
        migrations.RemoveField(
            model_name='writerfilmwork',
            name='film_work',
        ),
        migrations.RemoveField(
            model_name='writerfilmwork',
            name='writer',
        ),
        migrations.RemoveField(
            model_name='filmwork',
            name='directors',
        ),
        migrations.RemoveField(
            model_name='filmwork',
            name='writers',
        ),
        migrations.DeleteModel(
            name='Director',
        ),
        migrations.DeleteModel(
            name='DirectorFilmwork',
        ),
        migrations.DeleteModel(
            name='Writer',
        ),
        migrations.DeleteModel(
            name='WriterFilmwork',
        ),
    ]

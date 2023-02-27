# Generated by Django 3.2.13 on 2023-01-04 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_alter_personfilmwork_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personfilmwork',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.person', verbose_name='person_verbose_name'),
        ),
    ]

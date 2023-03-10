# Generated by Django 4.1.7 on 2023-02-19 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filmwork',
            options={'verbose_name': 'film work', 'verbose_name_plural': 'film works'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'person', 'verbose_name_plural': 'perons'},
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='genres',
            field=models.ManyToManyField(through='movies.GenreFilmwork', to='movies.genre', verbose_name='genres'),
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='persons',
            field=models.ManyToManyField(through='movies.PersonFilmwork', to='movies.person', verbose_name='persons'),
        ),
    ]

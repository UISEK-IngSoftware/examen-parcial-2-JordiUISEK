# Generated by Django 4.2 on 2025-05-31 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('rating', models.FloatField()),
                ('duration', models.IntegerField()),
                ('genre', models.CharField(max_length=200)),
                ('poster', models.ImageField(upload_to='posters/')),
                ('description', models.TextField()),
                ('actors', models.ManyToManyField(related_name='acted_movies', to='movies.actor')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.director')),
            ],
        ),
        migrations.AddField(
            model_name='director',
            name='movies',
            field=models.ManyToManyField(related_name='directed_movies', to='movies.movie'),
        ),
    ]

# Generated by Django 4.0.3 on 2022-05-19 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_movie_runtime_alter_movie_vote_average'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='tagline',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
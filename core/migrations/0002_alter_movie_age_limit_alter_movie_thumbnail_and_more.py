# Generated by Django 4.0.3 on 2022-05-19 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='age_limit',
            field=models.CharField(blank=True, choices=[('Alle', 'Alle'), ('Børn', 'Børn')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='thumbnail',
            field=models.ImageField(blank=True, default='/thumbnails/default_thumbnail.jpg', null=True, upload_to='thumbnails'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='type',
            field=models.CharField(blank=True, choices=[('serie', 'Serie'), ('film', 'Film')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='age_limit',
            field=models.CharField(choices=[('Alle', 'Alle'), ('Børn', 'Børn')], max_length=15),
        ),
    ]
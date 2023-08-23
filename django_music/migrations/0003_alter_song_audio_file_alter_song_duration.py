# Generated by Django 4.2.4 on 2023-08-23 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_music', '0002_album_created_at_alter_album_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='audio_file',
            field=models.FileField(blank=True, null=True, upload_to='songs/'),
        ),
        migrations.AlterField(
            model_name='song',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
# Generated by Django 3.0.5 on 2020-05-22 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poems', '0014_poet_custom_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='poem',
            name='poem_audio',
            field=models.FileField(blank=True, null=True, upload_to='poems/audio'),
        ),
    ]

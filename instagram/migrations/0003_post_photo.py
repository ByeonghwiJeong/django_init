# Generated by Django 3.2.13 on 2022-04-26 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0002_post_is_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]

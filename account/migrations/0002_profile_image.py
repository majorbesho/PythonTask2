# Generated by Django 4.2.5 on 2023-09-27 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default=1, upload_to='profile', verbose_name='profile'),
            preserve_default=False,
        ),
    ]

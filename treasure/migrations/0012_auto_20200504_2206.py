# Generated by Django 3.0.2 on 2020-05-04 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treasure', '0011_merge_20200504_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='audio',
            field=models.FileField(default='audio/audios/default.mp3', upload_to='audio'),
        ),
        migrations.AlterField(
            model_name='level',
            name='image',
            field=models.ImageField(default='images/images/level1.jpg', upload_to='images'),
        ),
    ]

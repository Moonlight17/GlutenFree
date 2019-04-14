# Generated by Django 2.2 on 2019-04-13 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gluten', '0003_auto_20190413_2225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='department',
        ),
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='default.png', upload_to='media'),
        ),
        migrations.AddField(
            model_name='profile',
            name='quantity',
            field=models.IntegerField(default=0, verbose_name='Количество рецептов'),
            preserve_default=False,
        ),
    ]

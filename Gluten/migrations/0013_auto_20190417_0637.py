# Generated by Django 2.2 on 2019-04-17 06:37

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Gluten', '0012_auto_20190417_0618'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Like',
            new_name='LikeRecept',
        ),
    ]
# Generated by Django 2.1.3 on 2020-09-25 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200925_0340'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='make_ads',
            new_name='advert_this',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='make_post',
            new_name='post_this',
        ),
    ]

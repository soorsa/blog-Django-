# Generated by Django 2.1.3 on 2020-09-25 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ad_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='ad_title',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='make_ads',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='make_post',
            field=models.BooleanField(default=True),
        ),
    ]

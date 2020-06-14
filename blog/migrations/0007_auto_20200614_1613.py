# Generated by Django 3.0.4 on 2020-06-14 20:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blogpost_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogpost',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

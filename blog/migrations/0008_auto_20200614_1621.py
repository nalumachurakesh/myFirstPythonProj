# Generated by Django 3.0.4 on 2020-06-14 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200614_1613'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-published_date', '-updated', '-timestamp']},
        ),
    ]
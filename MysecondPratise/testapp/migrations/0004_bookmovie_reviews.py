# Generated by Django 3.1.3 on 2021-02-12 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_bookmovie'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmovie',
            name='reviews',
            field=models.TextField(default=''),
        ),
    ]
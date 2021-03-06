# Generated by Django 3.1.3 on 2021-02-07 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='movie/images')),
                ('price', models.FloatField(default=0)),
                ('cast', models.CharField(max_length=100)),
                ('year_of_production', models.DateField()),
                ('slug', models.CharField(default='', max_length=200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.mycategory')),
                ('language', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='testapp.mylanguges')),
            ],
        ),
    ]

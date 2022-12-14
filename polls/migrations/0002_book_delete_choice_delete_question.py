# Generated by Django 4.1.2 on 2022-10-14 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('cat', models.CharField(max_length=200)),
                ('keyword', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('publisher', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]

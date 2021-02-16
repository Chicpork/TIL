# Generated by Django 3.1.6 on 2021-02-10 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giftcard', '0006_crawlerprocess_args'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchFilter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_run', models.BooleanField()),
                ('keyword', models.TextField()),
                ('min_price', models.IntegerField()),
                ('max_price', models.IntegerField()),
            ],
        ),
    ]
# Generated by Django 3.1.6 on 2021-02-08 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('giftcard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='giftcard',
            old_name='link',
            new_name='url',
        ),
    ]

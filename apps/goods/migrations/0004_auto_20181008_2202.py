# Generated by Django 2.0.6 on 2018-10-08 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20181008_2156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goods',
            old_name='category',
            new_name='categorys',
        ),
    ]
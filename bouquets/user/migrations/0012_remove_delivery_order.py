# Generated by Django 2.2.2 on 2019-06-25 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_auto_20190625_0633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery',
            name='order',
        ),
    ]

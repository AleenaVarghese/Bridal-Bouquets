# Generated by Django 2.2.2 on 2019-06-24 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productAdd', '0013_auto_20190624_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='productAdd.Product'),
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-09 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='URL',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-10 02:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_book_favorite_books'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='URL',
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='favorite_books',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='book',
            name='group',
            field=models.ManyToManyField(related_name='book', to='books.group'),
        ),
    ]

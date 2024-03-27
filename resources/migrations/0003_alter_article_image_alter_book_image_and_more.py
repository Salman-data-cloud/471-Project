# Generated by Django 5.0.2 on 2024-03-18 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_article_podcast_alter_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='resources/files/covers'),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='resources/files/covers'),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='image',
            field=models.ImageField(upload_to='resources/files/covers'),
        ),
    ]

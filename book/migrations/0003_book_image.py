# Generated by Django 3.2 on 2022-08-08 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20220724_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='Image',
            field=models.ImageField(blank=True, upload_to='book_images'),
        ),
    ]

# Generated by Django 3.2.4 on 2021-06-16 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20210616_2348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='books',
        ),
        migrations.AddField(
            model_name='cart',
            name='books',
            field=models.ManyToManyField(to='book.Book'),
        ),
    ]

# Generated by Django 4.2.8 on 2023-12-12 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advance_serilize', '0003_author_publisher_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book_publisher', to='advance_serilize.publisher'),
        ),
    ]

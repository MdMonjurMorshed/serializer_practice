# Generated by Django 4.2.8 on 2023-12-10 21:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('advance_serilize', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='firstmodel',
            name='id',
        ),
        migrations.AlterField(
            model_name='firstmodel',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 4.1.6 on 2023-05-17 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cb', '0017_complaint_favorites_complaintfavorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='verified',
            field=models.BooleanField(default=False, null=True),
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-19 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cb', '0018_profile_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='complaint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='cb.complaint'),
        ),
        migrations.AlterField(
            model_name='complaintfavorite',
            name='complaint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cb.complaint'),
        ),
    ]

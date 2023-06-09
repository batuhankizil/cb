# Generated by Django 4.1.6 on 2023-05-10 23:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cb', '0016_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='favorites',
            field=models.ManyToManyField(blank=True, related_name='favorite_complaints', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ComplaintFavorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_title', models.TextField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('complaint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cb.complaint')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 2.2.8 on 2019-12-18 12:27

import articles.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('writer', models.CharField(max_length=100, verbose_name='Writer')),
                ('genre', models.CharField(choices=[('adventure', 'Adventure'), ('fiction', 'Fiction'), ('non_fiction', 'Non Fiction'), ('technology', 'Technology'), ('lifestyle', 'Lifestyle')], max_length=20, verbose_name='Genre')),
                ('published_on', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Published on')),
                ('modified_on', models.DateTimeField(auto_now=True, verbose_name='')),
                ('title_image', models.ImageField(blank=True, null=True, upload_to=articles.models.upload_image, verbose_name='Title Image')),
            ],
        ),
    ]

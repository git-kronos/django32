# Generated by Django 3.2.6 on 2021-08-28 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_article_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]

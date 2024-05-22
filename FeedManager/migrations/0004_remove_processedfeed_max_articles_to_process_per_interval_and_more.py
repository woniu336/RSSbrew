# Generated by Django 5.0.6 on 2024-05-22 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FeedManager', '0003_alter_article_url_alter_processedfeed_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='processedfeed',
            name='max_articles_to_process_per_interval',
        ),
        migrations.AddField(
            model_name='processedfeed',
            name='articles_to_summarize_per_interval',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

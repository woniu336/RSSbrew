# Generated by Django 5.0.6 on 2024-05-28 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FeedManager', '0013_remove_processedfeed_digest_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processedfeed',
            name='last_digest',
            field=models.DateTimeField(blank=True, default=None, help_text='Last time the digest was generated, change if you want to reset the digest timer or force a new digest.', null=True),
        ),
    ]

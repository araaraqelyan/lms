# Generated by Django 5.0.3 on 2024-04-24 19:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAuth', '0004_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open_registration', models.BooleanField(default=True)),
                ('invitation_link_expiration', models.DurationField(default=datetime.timedelta(days=3))),
                ('verification_link_expiration', models.DurationField(default=datetime.timedelta(seconds=18000))),
            ],
        ),
    ]

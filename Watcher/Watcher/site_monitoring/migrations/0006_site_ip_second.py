# Generated by Django 3.0.5 on 2020-04-21 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_monitoring', '0005_auto_20200421_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='ip_second',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
    ]

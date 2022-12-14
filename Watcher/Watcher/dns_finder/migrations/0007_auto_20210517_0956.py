# Generated by Django 3.2 on 2021-05-31 14:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dns_finder', '0006_auto_20201125_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='dnsmonitored',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='dnstwisted',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='KeywordMonitored',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Corporate Keyword',
                'verbose_name_plural': 'Corporate Keywords Monitored',
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='dnstwisted',
            name='dns_monitored',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dns_finder.dnsmonitored'),
        ),
        migrations.AddField(
            model_name='dnstwisted',
            name='keyword_monitored',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dns_finder.keywordmonitored'),
        ),
    ]

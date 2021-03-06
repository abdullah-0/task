# Generated by Django 4.0.1 on 2022-01-15 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Metrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('channel', models.CharField(choices=[('adcolony', 'adcolony'), ('apple_search_ads', 'apple_search_ads'), ('chartboost', 'chartboost'), ('facebook', 'facebook'), ('google', 'google'), ('unityads', 'unityads'), ('vungle', 'vungle')], max_length=16)),
                ('country', models.CharField(choices=[('US', 'US'), ('DE', 'DE'), ('GB', 'GB'), ('CA', 'CA'), ('FR', 'FR')], max_length=2)),
                ('os', models.CharField(choices=[('android', 'android'), ('ios', 'ios')], max_length=7)),
                ('impressions', models.PositiveIntegerField()),
                ('clicks', models.PositiveIntegerField()),
                ('installs', models.PositiveIntegerField()),
                ('spend', models.DecimalField(decimal_places=3, max_digits=8)),
                ('revenue', models.DecimalField(decimal_places=3, max_digits=8)),
            ],
        ),
    ]

# Generated by Django 5.1.6 on 2025-02-17 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=60)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('logo', models.ImageField(upload_to='company_logos/')),
                ('const_center', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companys',
            },
        ),
    ]

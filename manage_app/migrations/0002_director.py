# Generated by Django 5.0 on 2023-12-13 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
    ]

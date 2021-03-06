# Generated by Django 4.0.4 on 2022-05-03 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Title')),
                ('code', models.TextField(blank=True, verbose_name='Code')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
            ],
        ),
    ]

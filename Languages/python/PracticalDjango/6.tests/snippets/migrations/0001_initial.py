# Generated by Django 4.0.4 on 2022-05-06 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SnippetModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('code', models.CharField(max_length=128)),
                ('description', models.TextField()),
            ],
        ),
    ]
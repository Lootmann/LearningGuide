# Generated by Django 4.0.4 on 2022-05-26 02:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SnippetModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='snippet_id')),
                ('title', models.CharField(max_length=128, verbose_name='Title')),
                ('code', models.TextField(blank=True, verbose_name='Code')),
            ],
        ),
    ]
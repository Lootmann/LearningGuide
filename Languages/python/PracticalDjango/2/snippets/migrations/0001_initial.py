# Generated by Django 4.0.4 on 2022-04-29 13:18

from django.db import migrations, models
import django.db.models.deletion


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
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='PostedAt')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='UpdatedAt')),
            ],
            options={
                'verbose_name': 'snippet',
                'verbose_name_plural': 'snippets',
                'db_table': 'snippets',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='TagName')),
                ('snippets', models.ManyToManyField(related_name='tags', related_query_name='tag', to='snippets.snippet')),
            ],
            options={
                'db_table': 'tags',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Sentence')),
                ('commented_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snippets.snippet', verbose_name='snippet')),
            ],
            options={
                'db_table': 'comments',
            },
        ),
    ]

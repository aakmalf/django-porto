# Generated by Django 4.2.4 on 2023-08-19 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projects',
            options={},
        ),
        migrations.AddField(
            model_name='projects',
            name='categories',
            field=models.ManyToManyField(to='projects.category'),
        ),
        migrations.AddField(
            model_name='projects',
            name='description',
            field=models.TextField(default='tes', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projects',
            name='link',
            field=models.URLField(default='blank'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projects',
            name='published',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='title',
            field=models.CharField(default='blank', max_length=60),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projects',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-04 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_alter_article_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default='djangodbmodelsfieldscharfield', max_length=255),
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-02 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_article_excerpt_alter_article_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='excerpt',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
# Generated by Django 4.0.3 on 2022-03-02 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_article_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='excerpt',
            field=models.CharField(default='', max_length=50),
        ),
    ]
# Generated by Django 4.0.3 on 2022-03-02 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_article_excerpt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('featured_genre', models.PositiveSmallIntegerField(default=1)),
            ],
        ),
    ]

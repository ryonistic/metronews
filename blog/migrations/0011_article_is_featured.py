# Generated by Django 4.0.3 on 2022-03-02 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_delete_feature'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]

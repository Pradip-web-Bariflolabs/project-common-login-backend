# Generated by Django 5.0 on 2023-12-26 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_user_user_docs_remove_user_user_pic_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_category',
            field=models.CharField(default=10, max_length=100),
            preserve_default=False,
        ),
    ]

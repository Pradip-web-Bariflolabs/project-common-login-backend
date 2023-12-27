# Generated by Django 5.0 on 2023-12-26 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_docs',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_pic',
        ),
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.CharField(default=10, max_length=100),
            preserve_default=False,
        ),
    ]

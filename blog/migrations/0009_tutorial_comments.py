# Generated by Django 2.1.7 on 2019-09-10 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='comments',
            field=models.IntegerField(default=0),
        ),
    ]

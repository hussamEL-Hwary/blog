# Generated by Django 2.1.7 on 2019-09-10 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_tutorial_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='img_url',
            field=models.CharField(max_length=250, null=True),
        ),
    ]

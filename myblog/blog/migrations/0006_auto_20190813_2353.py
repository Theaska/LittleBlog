# Generated by Django 2.2.4 on 2019-08-13 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190813_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author_nickname',
            field=models.CharField(default=None, max_length=100),
        ),
    ]

# Generated by Django 2.0.3 on 2019-02-09 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0009_auto_20190207_0009'),
    ]

    operations = [
        migrations.AddField(
            model_name='carttable',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
# Generated by Django 2.0.3 on 2019-01-10 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=40)),
            ],
        ),
    ]

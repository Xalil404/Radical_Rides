# Generated by Django 3.2.22 on 2023-11-13 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmessage',
            name='message',
            field=models.TextField(max_length=2000),
        ),
    ]
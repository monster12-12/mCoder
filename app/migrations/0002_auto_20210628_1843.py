# Generated by Django 3.2.4 on 2021-06-29 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=112, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.TextField(max_length=112, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=112, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=112, null=True),
        ),
    ]
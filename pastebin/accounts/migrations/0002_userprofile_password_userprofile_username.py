# Generated by Django 4.2.1 on 2024-01-23 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='password',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='username',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
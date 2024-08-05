# Generated by Django 4.2.1 on 2024-01-23 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile_password_userprofile_username'),
        ('pastes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paste',
            name='user',
        ),
        migrations.AddField(
            model_name='paste',
            name='user_profile',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile'),
            preserve_default=False,
        ),
    ]
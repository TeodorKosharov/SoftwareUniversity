# Generated by Django 4.1.3 on 2022-11-09 20:18

from django.db import migrations, models
import users_demos.auth_app.managers


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0002_appuser_groups_appuser_is_superuser_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='appuser',
            managers=[
                ('objects', users_demos.auth_app.managers.AppUserManager()),
            ],
        ),
        migrations.AddField(
            model_name='appuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]

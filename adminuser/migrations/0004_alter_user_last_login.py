# Generated by Django 4.0 on 2023-06-15 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminuser', '0003_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-16 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_user_numverification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
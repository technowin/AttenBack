# Generated by Django 4.2.7 on 2024-03-14 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_user_first_name_user_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]

# Generated by Django 4.1.3 on 2023-06-28 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_alter_account_user_alter_user_verification_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="verification_code",
            field=models.CharField(default="106414", max_length=6, unique=True),
        ),
    ]

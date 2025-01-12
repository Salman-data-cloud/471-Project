# Generated by Django 5.0.1 on 2024-04-18 19:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ("user_profile", "0002_rename_location_profile_address_and_more"),
        # Adjust the dependency to the correct preceding migration
        # For example, if "0002_alter_profile_user" is the correct preceding migration,
        # then replace "0001_initial" with "0002_alter_profile_user"
    ]

    operations = [
        migrations.AddField(
            model_name="profile", name="id_user", field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name="profile",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]


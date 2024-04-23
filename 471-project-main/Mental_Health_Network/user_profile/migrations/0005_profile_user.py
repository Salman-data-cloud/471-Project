from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_profile",  "0003_rename_address_profile_location_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="user",  # Removed adding user field
        ),
    ]

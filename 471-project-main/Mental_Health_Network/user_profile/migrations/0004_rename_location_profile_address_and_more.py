from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_profile", "0003_rename_address_profile_location_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="user",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=models.CASCADE,  # Changed to models.CASCADE
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]



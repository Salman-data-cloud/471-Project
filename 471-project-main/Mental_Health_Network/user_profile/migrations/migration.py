import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_profile", "0006_alter_profile_user"),

    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=models.CASCADE, to='Login_Authentication.UserLoginAuth'),
        ),
    ]
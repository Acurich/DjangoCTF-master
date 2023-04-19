

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0002_challenge_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='challenge',
            old_name='day_created',
            new_name='date_created',
        ),
    ]

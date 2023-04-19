
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_room_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='name',
            new_name='title',
        ),
    ]

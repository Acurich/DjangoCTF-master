

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_room'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Room',
            new_name='Post',
        ),
    ]

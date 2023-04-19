

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_name_post_title'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]

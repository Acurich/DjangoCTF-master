

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_delete_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Challenge',
        ),
    ]


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0008_alter_note_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['-date']},
        ),
    ]

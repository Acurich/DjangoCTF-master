

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0009_alter_note_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='date',
            field=models.DateField(),
        ),
    ]

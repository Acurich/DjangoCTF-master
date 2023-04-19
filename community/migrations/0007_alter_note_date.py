
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0006_alter_note_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

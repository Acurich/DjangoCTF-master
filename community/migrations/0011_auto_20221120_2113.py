
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0010_alter_note_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='f',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='date',
            field=models.DateTimeField(),
        ),
    ]

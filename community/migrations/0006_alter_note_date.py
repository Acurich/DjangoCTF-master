

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0005_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

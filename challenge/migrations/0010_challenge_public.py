

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0009_delete_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='public',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]

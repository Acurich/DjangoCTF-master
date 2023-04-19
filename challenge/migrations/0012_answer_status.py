

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0011_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='status',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]

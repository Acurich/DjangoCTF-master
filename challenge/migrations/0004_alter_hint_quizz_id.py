

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0003_rename_day_created_challenge_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hint',
            name='quizz_id',
            field=models.IntegerField(default=96),
            preserve_default=False,
        ),
    ]

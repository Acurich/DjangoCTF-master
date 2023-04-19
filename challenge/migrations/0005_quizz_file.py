

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0004_alter_hint_quizz_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizz',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]



from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0005_quizz_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizz',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
    ]

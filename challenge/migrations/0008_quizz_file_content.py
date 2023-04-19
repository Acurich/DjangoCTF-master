

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0007_auto_20221214_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizz',
            name='file_content',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
    ]

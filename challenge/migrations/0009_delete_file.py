

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0008_quizz_file_content'),
    ]

    operations = [
        migrations.DeleteModel(
            name='File',
        ),
    ]



from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0006_alter_quizz_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quizz_id', models.IntegerField()),
                ('file_content', models.FileField(upload_to='files/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='quizz',
            name='file',
        ),
    ]



from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0010_challenge_public'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=20, null=True)),
                ('challenge_id', models.IntegerField()),
                ('quizz_id', models.IntegerField()),
                ('answer', models.TextField()),
                ('point', models.IntegerField()),
            ],
        ),
    ]



from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('day_created', models.DateTimeField(auto_now_add=True)),
                ('date_start', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quizz_id', models.CharField(blank=True, max_length=10, null=True)),
                ('content', models.TextField()),
                ('point', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Quizz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('challenge_id', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('point', models.IntegerField()),
            ],
        ),
    ]

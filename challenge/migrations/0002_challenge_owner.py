
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='owner',
            field=models.CharField(default='chien', max_length=200),
            preserve_default=False,
        ),
    ]

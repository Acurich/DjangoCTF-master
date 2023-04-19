

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_auto_20221105_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='main/images/avatar.svg', null=True, upload_to=''),
        ),
    ]

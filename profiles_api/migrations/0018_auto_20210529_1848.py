# Generated by Django 2.2 on 2021-05-29 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0017_auto_20210529_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singlequbitgate',
            name='params',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
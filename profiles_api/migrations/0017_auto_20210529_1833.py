# Generated by Django 2.2 on 2021-05-29 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0016_auto_20210529_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singlequbitgate',
            name='params',
            field=models.TextField(null=True),
        ),
    ]
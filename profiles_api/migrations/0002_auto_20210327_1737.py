# Generated by Django 2.2 on 2021-03-27 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestdata',
            name='no_qubits',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='requestdata',
            name='shots',
            field=models.PositiveIntegerField(),
        ),
    ]
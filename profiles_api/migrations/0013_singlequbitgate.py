# Generated by Django 2.2 on 2021-05-24 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0012_auto_20210517_1804'),
    ]

    operations = [
        migrations.CreateModel(
            name='SingleQubitGate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('qubits', models.TextField()),
                ('params', models.TextField()),
            ],
        ),
    ]

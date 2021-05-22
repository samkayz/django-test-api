# Generated by Django 3.2.3 on 2021-05-22 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KeyValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uiid', models.UUIDField(auto_created=True)),
                ('date_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'key_value',
            },
        ),
    ]
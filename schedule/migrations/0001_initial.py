# Generated by Django 3.2.13 on 2022-07-08 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regdate', models.TextField()),
                ('time', models.CharField(max_length=10)),
                ('gudan1', models.CharField(max_length=15)),
                ('gudan2', models.CharField(max_length=15)),
            ],
        ),
    ]
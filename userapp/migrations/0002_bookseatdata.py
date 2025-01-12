# Generated by Django 5.1.1 on 2024-10-16 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookSeatData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.IntegerField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('nop', models.IntegerField()),
            ],
        ),
    ]

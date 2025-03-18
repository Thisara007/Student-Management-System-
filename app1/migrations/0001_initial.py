# Generated by Django 5.1.7 on 2025-03-15 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('regno', models.IntegerField()),
                ('register_date', models.DateField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]

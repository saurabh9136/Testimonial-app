# Generated by Django 5.0.6 on 2024-05-14 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('emp_id', models.CharField(max_length=5)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=256)),
                ('working', models.BooleanField(default=True)),
                ('department', models.CharField(max_length=20)),
            ],
        ),
    ]

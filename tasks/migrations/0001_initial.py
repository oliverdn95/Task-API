# Generated by Django 5.1.5 on 2025-01-28 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Task', max_length=100)),
                ('status', models.CharField(default='To Do', max_length=7)),
                ('priority', models.CharField(max_length=6)),
                ('complexity', models.CharField(max_length=6)),
                ('summary', models.CharField(default=models.CharField(default='Task', max_length=100), max_length=500)),
            ],
        ),
    ]

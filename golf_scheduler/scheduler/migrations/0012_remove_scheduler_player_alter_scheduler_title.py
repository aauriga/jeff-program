# Generated by Django 4.2.1 on 2023-07-28 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0011_alter_scheduler_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheduler',
            name='Player',
        ),
        migrations.AlterField(
            model_name='scheduler',
            name='title',
            field=models.CharField(default='task-2023_07_28_16_57_14', max_length=200),
        ),
    ]

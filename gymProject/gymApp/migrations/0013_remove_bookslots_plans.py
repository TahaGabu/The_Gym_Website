# Generated by Django 4.2.4 on 2023-09-18 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymApp', '0012_bookslots_plans'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookslots',
            name='plans',
        ),
    ]
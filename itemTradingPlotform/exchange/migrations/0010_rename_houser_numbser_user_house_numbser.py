# Generated by Django 3.2 on 2022-10-09 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0009_alter_requirement_material_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='houser_numbser',
            new_name='house_numbser',
        ),
    ]
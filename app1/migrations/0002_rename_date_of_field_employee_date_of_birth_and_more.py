# Generated by Django 5.0.7 on 2024-07-25 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='date_of_field',
            new_name='date_of_birth',
        ),
        migrations.AlterField(
            model_name='employee',
            name='skills',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

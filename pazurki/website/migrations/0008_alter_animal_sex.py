# Generated by Django 4.2.7 on 2023-12-04 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_alter_animal_name_alter_animal_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='sex',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6, null=True),
        ),
    ]

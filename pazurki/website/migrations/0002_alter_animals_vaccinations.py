# Generated by Django 4.2.7 on 2023-12-04 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animals',
            name='vaccinations',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], null=True),
        ),
    ]
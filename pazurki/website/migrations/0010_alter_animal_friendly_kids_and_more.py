# Generated by Django 4.2.7 on 2023-12-04 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_connector'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='friendly_kids',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], null=True),
        ),
        migrations.AlterField(
            model_name='animal',
            name='friendly_others',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], null=True),
        ),
        migrations.AlterField(
            model_name='animal',
            name='sterilization',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], null=True),
        ),
    ]

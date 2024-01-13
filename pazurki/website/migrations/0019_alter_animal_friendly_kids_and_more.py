# Generated by Django 4.2.7 on 2024-01-10 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_remove_adopt_form_id_adoptee_alter_animal_breed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='friendly_kids',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=6, null=True, verbose_name='Friendly to kids'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='friendly_others',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=6, null=True, verbose_name='Friendly to other animals'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='sterilization',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=6, null=True, verbose_name='Sterilized'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='vaccinations',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=6, null=True, verbose_name='Vaccinated'),
        ),
    ]

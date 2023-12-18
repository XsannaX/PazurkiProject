# Generated by Django 4.2.7 on 2023-12-14 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_alter_workers_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='adopt_form',
            name='status',
            field=models.CharField(choices=[('Processing', 'Processing'), ('Adopted', 'Adopted')], default='Processing', max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='adopt_form',
            name='animal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.animal'),
        ),
    ]
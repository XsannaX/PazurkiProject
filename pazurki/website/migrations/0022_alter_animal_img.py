# Generated by Django 4.2.7 on 2024-01-13 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0021_alter_animal_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='img',
            field=models.ImageField(blank=True, default='pfp2.jpg', upload_to='animal_pics/'),
        ),
    ]

# Generated by Django 5.1.7 on 2025-03-15 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_tw', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='../static/photos'),
        ),
        migrations.AlterField(
            model_name='project',
            name='technology',
            field=models.CharField(max_length=50),
        ),
    ]

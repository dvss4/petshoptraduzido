# Generated by Django 4.1.6 on 2023-03-16 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_ofereceservico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='sexo',
            field=models.CharField(choices=[('easy', 'easy'), ('medium', 'medium'), ('hard', 'hard')], max_length=6),
        ),
    ]
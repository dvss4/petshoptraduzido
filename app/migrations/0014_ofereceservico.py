# Generated by Django 4.1.7 on 2023-03-13 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_fazpedido_unique_together_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfereceServico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cd_Empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.empresa')),
                ('Cod_servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.servico')),
            ],
        ),
    ]

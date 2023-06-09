# Generated by Django 4.1.7 on 2023-03-12 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_empresa'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecebePedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cdEmpresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.empresa')),
                ('id_pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pedido')),
            ],
            options={
                'unique_together': {('cdEmpresa', 'id_pedido')},
            },
        ),
    ]

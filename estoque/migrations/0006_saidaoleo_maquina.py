# Generated by Django 2.2.7 on 2019-11-07 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0005_maquina'),
    ]

    operations = [
        migrations.AddField(
            model_name='saidaoleo',
            name='maquina',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='oleos', to='estoque.Maquina'),
            preserve_default=False,
        ),
    ]

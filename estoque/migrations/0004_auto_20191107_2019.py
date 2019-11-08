# Generated by Django 2.2.7 on 2019-11-07 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0003_auto_20191107_2008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entradaoleo',
            old_name='numero_notafiscal',
            new_name='nota_fiscal',
        ),
        migrations.RenameField(
            model_name='saidaoleo',
            old_name='resposavel',
            new_name='responsavel',
        ),
        migrations.AlterField(
            model_name='entradaoleo',
            name='oleo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entradas', to='estoque.Oleo', verbose_name='óleo'),
        ),
    ]

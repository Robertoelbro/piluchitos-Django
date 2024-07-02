# Generated by Django 5.0.6 on 2024-06-30 23:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id_marca', models.AutoField(db_column='idMarca', primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codprod', models.AutoField(db_column='idProducto', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('titulo', models.CharField(max_length=60)),
                ('descripcion', models.TextField(max_length=700)),
                ('foto', models.ImageField(upload_to='')),
                ('stock', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('fec_salida', models.DateField()),
                ('marca', models.ForeignKey(db_column='idMarca', on_delete=django.db.models.deletion.CASCADE, to='producto.marca')),
            ],
        ),
    ]

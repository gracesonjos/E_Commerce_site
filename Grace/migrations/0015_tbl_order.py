# Generated by Django 4.2 on 2023-05-05 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Grace', '0014_idgen_orderid'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_order',
            fields=[
                ('order_id', models.CharField(max_length=225, primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=225)),
                ('order_date', models.CharField(max_length=200)),
                ('oder_quandity', models.IntegerField()),
                ('coustomer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Grace.tbl_coustomer')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Grace.tbl_product')),
            ],
            options={
                'db_table': 'tbl_order',
            },
        ),
    ]
# Generated by Django 4.2 on 2023-05-02 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Grace', '0003_idgen_shopeid'),
    ]

    operations = [
        migrations.AddField(
            model_name='idgen',
            name='productid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='tbl_product',
            fields=[
                ('product_id', models.CharField(max_length=225, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=200)),
                ('photo', models.CharField(max_length=225)),
                ('stock', models.IntegerField()),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Grace.tbl_category')),
            ],
            options={
                'db_table': 'tbl_product',
            },
        ),
    ]

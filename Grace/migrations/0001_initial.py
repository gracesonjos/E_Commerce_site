# Generated by Django 4.2 on 2023-05-01 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='idgen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryid', models.IntegerField()),
            ],
            options={
                'db_table': 'idgen',
            },
        ),
        migrations.CreateModel(
            name='tbl_category',
            fields=[
                ('category_id', models.CharField(max_length=400, primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=100)),
                ('photo', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=50000)),
            ],
            options={
                'db_table': 'tbl_category',
            },
        ),
        migrations.CreateModel(
            name='tbl_shope',
            fields=[
                ('shope_id', models.CharField(max_length=400, primary_key=True, serialize=False)),
                ('shope_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('pincode', models.IntegerField()),
                ('phone_number', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
                ('photo', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'tbl_shope',
            },
        ),
    ]

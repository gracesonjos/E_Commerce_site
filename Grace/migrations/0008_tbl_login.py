# Generated by Django 4.2 on 2023-05-04 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Grace', '0007_tbl_coustomer'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_login',
            fields=[
                ('username', models.CharField(max_length=225, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'tbl_login',
            },
        ),
    ]

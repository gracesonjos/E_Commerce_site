# Generated by Django 4.2 on 2023-05-08 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Grace', '0019_idgen_agentid'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_order',
            name='total_amount',
            field=models.IntegerField(default=2000),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.0.7 on 2022-11-03 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_description_alter_order_transcation_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='transcation_id',
            field=models.CharField(default='CAA13', editable=False, max_length=50),
        ),
    ]

# Generated by Django 3.1.7 on 2021-04-14 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_order_orderitem_shippingadress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_ordered',
            field=models.DateTimeField(auto_created=True, null=True),
        ),
    ]
